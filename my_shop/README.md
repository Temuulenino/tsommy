# Flask лаборатори — NINO SHOP

## Ажиллуулах (VS Code terminal / PowerShell)
```powershell
.\.venv\Scripts\python.exe lab8.py
```
Дараа нь http://127.0.0.1:5000/ хаягийг хөтөч дээр нээнэ. Зогсоох: Ctrl+C.

Орчныг шинээр үүсгэх бол:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Лабораторийн шаардлагууд
- `/` — нүүр, баннер, онцлох бараа.
- `/store` — барааны жагсаалт.
- `/product` — эхний барааны дэлгэрэнгүй; `/product/2`, `/product/3` мөн ажиллана.
- `/cart` — сагсны харагдах загвар. Бараа хадгалах, захиалга, төлбөр хэрэгжүүлээгүй.
- `/hello` — Сайн уу, дэлхий!
- `/hello/Bat` — Сайн уу, Bat!
- HTML нь `templates`, CSS/зураг нь `static` дотор; холбоосууд `url_for` ашиглана.

## Кодын тайлбар
`@app.route` хаягийг Python функцтэй холбоно. `render_template` HTML боловсруулж, products/name зэрэг утга дамжуулна. `{{ name }}` утгыг харуулна; `{% if name %}` нэр байгаа эсэхийг шалгана. `base.html`-д нийтлэг цэс, CSS, хөл хэсэг бий. Бусад хуудас Jinja `extends` ашиглана.

## Бэлэн загвар ба эх сурвалж
Start Bootstrap — Shop Homepage (MIT): https://github.com/StartBootstrap/startbootstrap-shop-homepage
Татсан эх HTML: `reference/original-index.html`; лиценз: `reference/LICENSE`.
Загварын Bootstrap CSS болон card/grid/navbar бүтцийг ашиглаж, Монгол агуулга, Flask/Jinja хуудсанд тохируулсан. Нэмэлт CSS: `static/css/style.css`. SVG зургуудыг энэ төсөлд зориулан кодоор хийсэн. Бүх харагдах asset локал тул ажиллах үед CDN шаардахгүй.
Flask: https://flask.palletsprojects.com/en/stable/quickstart/

`debug=True` нь зөвхөн өөрийн компьютер дээр хөгжүүлэх зориулалттай.
