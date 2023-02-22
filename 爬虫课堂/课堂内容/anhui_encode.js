//沃特水务-前端加密/解密工具
//1.引用
//2.实例化 var waterSecurity = new WaterSecurity()
//3.调用属性 waterSecurity.version
//4.调用加密方法  waterSecurity.encode(webCode);
//5.调用解密方法 waterSecurity.decode(webCode)

var WaterSecurity = function () {
    this.init()
}
WaterSecurity.prototype = {
    version: '2.1',
    init: function () {
        //精确计算字符串长度
        String.prototype.gblen = function () {
            var len = 0;
            for (var i = 0; i < this.length; i++) {
                if (this.charCodeAt(i) > 127 || this.charCodeAt(i) == 94) {
                    len += 2;
                } else {
                    len++;
                }
            }
            return len;
        }
    },
    //加密
    encode: function (data) {
        this.print(data);
        data += ""
        if (data == "")
            return "";
        data = encodeURI(data).replace(/\+/g, "%2B");

        var length = data.gblen()
        if (length % 2 != 0) {
            data += "*";
        }
        this.print(data);
        data = this.parityTransposition(data);
        this.print(data);
        var result = this.version + this.utf16to8(this.base64encode(data));
        this.print(result);
        return result;
    },
    print: function (data) {
        //console.log(data);
    },
    //奇偶位换位
    parityTransposition: function (data) {
        var newData = [];
        for (var i = 0; i < data.length; i += 2) {
            newData.push(data[i + 1]);
            newData.push(data[i]);
        }
        newData = newData.join('')
        return newData;
    },

    //解密
    decode: function (data) {
        data += ""
        this.print(data);
        if (data == "")
            return "[]";
        if (this.version) {
            var versionS = data.substring(0, 3);
            if (versionS !== this.version) {
                return alert("加解密版本不一致！");
            }
            data = data.substring(3, data.length);
        }
        var endTag = data.substring(data.length - 4);
        var tagsStr = data.substring(data.indexOf(endTag)); //获取标签字符串
        var tags = new Array(); //存储标签值
        tagsStr = tagsStr.substring(4, tagsStr.length - 4);
        var content = new Array(); //存储标签与内容对
        for (var i = 0; 4 * i < tagsStr.length; i++) {
            var tag = tagsStr.substr(i * 4, 4);
            tags[i] = tag;
            content[tag] = null;
        }

        //按标记对号入座
        var positions = this.getTagsPosition(data, tags);
        var index = 0;
        for (var i = 0; i < positions.length; i++) {
            var msg = data.substring(index, positions[i]);
            var tag = data.substr(positions[i], 4);
            content[tag] = msg;
            index = positions[i] + 4;
        }

        var result = []; //将碎片组合
        for (var i = 0; i < tags.length; i++) {
            result.push(content[tags[i]]);
        }
        result = result.join('')
        result = this.utf8to16(this.base64decode(result))
        //result = decodeURI(result);
        return result;
    },
    //获取Tag位置，并按照从小到大的顺序排序
    getTagsPosition: function (data, tags) {
        var positions = new Array();
        for (i = 0; i < tags.length; i++) {
            positions[i] = data.indexOf(tags[i])
        }
        return positions.sort(function (a, b) {
            return a > b ? 1 : -1
        });
    },
    base64EncodeChars: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
    base64DecodeChars: new Array(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1),

    base64encode: function (str) {
        var out, i, len;
        var c1, c2, c3;

        len = str.length;
        i = 0;
        out = [];
        while (i < len) {
            c1 = str.charCodeAt(i++) & 0xff;
            if (i == len) {
                out.push(this.base64EncodeChars.charAt(c1 >> 2));
                out.push(this.base64EncodeChars.charAt((c1 & 0x3) << 4));
                out.push("==");
                break;
            }
            c2 = str.charCodeAt(i++);
            if (i == len) {
                out.push(this.base64EncodeChars.charAt(c1 >> 2));
                out.push(this.base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4)));
                out.push(this.base64EncodeChars.charAt((c2 & 0xF) << 2));
                out.push("=");
                break;
            }
            c3 = str.charCodeAt(i++);
            out.push(this.base64EncodeChars.charAt(c1 >> 2));
            out.push(this.base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4)));
            out.push(this.base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6)));
            out.push(this.base64EncodeChars.charAt(c3 & 0x3F));
        }
        return out.join('');
    },

    base64decode: function (str) {
        var c1, c2, c3, c4;
        var i, len, out;

        len = str.length;
        i = 0;
        out = [];
        while (i < len) {
            /* c1 */
            do {
                c1 = this.base64DecodeChars[str.charCodeAt(i++) & 0xff];
            } while (i < len && c1 == -1);
            if (c1 == -1)
                break;

            /* c2 */
            do {
                c2 = this.base64DecodeChars[str.charCodeAt(i++) & 0xff];
            } while (i < len && c2 == -1);
            if (c2 == -1)
                break;

            out.push(String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4)));

            /* c3 */
            do {
                c3 = str.charCodeAt(i++) & 0xff;
                if (c3 == 61)
                    return out.join('');
                c3 = this.base64DecodeChars[c3];
            } while (i < len && c3 == -1);
            if (c3 == -1)
                break;

            out.push(String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2)));

            /* c4 */
            do {
                c4 = str.charCodeAt(i++) & 0xff;
                if (c4 == 61)
                    return out.join('');
                c4 = this.base64DecodeChars[c4];
            } while (i < len && c4 == -1);
            if (c4 == -1)
                break;
            out.push(String.fromCharCode(((c3 & 0x03) << 6) | c4));
        }
        return out.join('');
    },

    utf16to8: function (str) {
        var out, i, len, c;

        out = [];
        len = str.length;
        for (i = 0; i < len; i++) {
            c = str.charCodeAt(i);
            if ((c >= 0x0001) && (c <= 0x007F)) {
                out.push(str.charAt(i));
            } else if (c > 0x07FF) {
                out.push(String.fromCharCode(0xE0 | ((c >> 12) & 0x0F)));
                out.push(String.fromCharCode(0x80 | ((c >> 6) & 0x3F)));
                out.push(String.fromCharCode(0x80 | ((c >> 0) & 0x3F)));
            } else {
                out.push(String.fromCharCode(0xC0 | ((c >> 6) & 0x1F)));
                out.push(String.fromCharCode(0x80 | ((c >> 0) & 0x3F)));
            }
        }
        return out.join('');
    },

    utf8to16: function (str) {
        var out, i, len, c;
        var char2, char3;

        out = [];
        len = str.length;
        i = 0;
        while (i < len) {
            c = str.charCodeAt(i++);
            switch (c >> 4) {
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                    // 0xxxxxxx  
                    out.push(str.charAt(i - 1));
                    break;
                case 12:
                case 13:
                    // 110x xxxx   10xx xxxx  
                    char2 = str.charCodeAt(i++);
                    out.push(String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F)));
                    break;
                case 14:
                    // 1110 xxxx  10xx xxxx  10xx xxxx  
                    char2 = str.charCodeAt(i++);
                    char3 = str.charCodeAt(i++);
                    out.push(String.fromCharCode(((c & 0x0F) << 12) |
                        ((char2 & 0x3F) << 6) |
                        ((char3 & 0x3F) << 0)));
                    break;
            }
        }

        return out.join('');
    },

}
var waterSecurity = new WaterSecurity()
// 调用加密方法
function waterEncode(data) {
    return waterSecurity.encode(data)
}
//调用解密方法
function waterDecode(data) {
    return waterSecurity.decode(data)

}