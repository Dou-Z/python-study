import js2py

js = js2py.EvalJs()

with open('baidu.js', 'r') as f:
    # JS_data = f.read()
    js.execute(f.read())

js_con = '我'
sign = js.e(js_con)
print(sign)