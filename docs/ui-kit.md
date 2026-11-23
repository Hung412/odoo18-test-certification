# Bộ khung giao diện mô phỏng (câu hỏi có hình)

Câu hỏi có hình dùng trường `"image"`: một đoạn HTML vẽ lại màn hình Odoo 18 bằng các class `ox-*` có sẵn trong `src/template.html`.
Hình luôn hiển thị như ảnh chụp giao diện sáng, kể cả khi trang đang ở chế độ tối.

## Quy tắc

- Bọc toàn bộ trong `<div class="ox">…</div>`. Không dùng `<script>`, ảnh ngoài, `<img>`, `<style>` hay link.
- Chỉ dùng các class bên dưới. Được thêm `style="…"` nội tuyến cho bố cục (độ rộng, khoảng cách, màu chữ).
- Giữ ngắn: tối đa khoảng 3.000 ký tự, chỉ vẽ phần màn hình cần cho câu hỏi.
- Dữ liệu là dữ liệu demo của Odoo (Deco Addict, Azure Interior, Gemini Furniture, [FURN_xxxx]…), không dùng tên công ty hay người thật.
- Khi câu hỏi trỏ vào một vị trí trên hình, đánh dấu bằng `<span class="ox-mark">1</span>` (hoặc `ox-hl` để viền đỏ) và gọi trong câu hỏi là "marker 1".
- Hình phải đúng với Odoo 18: tên menu, nút, trạng thái, nhãn trường.

## Thành phần

| Nhóm | Class |
|---|---|
| Khung | `ox` (gốc), `ox-nav` (thanh menu; `ox-app` = tên app), `ox-cp` (control panel: 2 `div` trái/phải), `ox-body` (nền xám quanh form) |
| Control panel | `ox-bc` (breadcrumb: `<a>` mục cha, `<b>` mục hiện tại), `ox-search` + `ox-facet` (bộ lọc đang bật), `ox-views` (các `span`, `on` = view đang chọn), `ox-pager` |
| Nút | `ox-btn` + `ox-primary` / `ox-link` / `ox-danger` |
| Form | `ox-bar` (hàng nút + statusbar), `ox-status` (các `span`, `on` = trạng thái hiện tại), `ox-sheet`, `ox-smarts` > `ox-smart` (`<b>số</b>nhãn`), `ox-ribbon` (+ `ok` / `info`), `ox-title` (+ `<small>`), `ox-fields` (2 cột, mỗi cột một `div`) > `ox-f` (`span.l` nhãn, `span.v` giá trị; `v ro` = chỉ đọc, `v req` = bắt buộc), `ox-tabs` (`span.on`) |
| Chatter | `ox-chatter` > `ox-cbar` (nút Send message / Log note / Activities), `ox-msg` (`ox-av` + nội dung `span.who`, `span.when`), `ox-note` |
| List | `table.ox-list` (`th`/`td`, `n` = cột số, `tr.grp` = dòng nhóm, `tr.sel` = dòng chọn, `tr.muted`, `tfoot` = tổng) |
| Kanban | `ox-kanban` > `ox-col` > `ox-colh` (+ `<small>`), `ox-prog` (`i.g` / `i.o` / `i.r` / `i.x` với `style="width:%"`), `ox-card` (`.t`, `.s`, `.foot`) |
| Nhỏ | `ox-tag c1…c6`, `ox-badge ok/warn/bad/info`, `ox-stars` (`<b>★★</b>★` = 2/3 sao), `ox-act late/today/planned/none` (biểu tượng activity: đỏ = quá hạn, cam = hôm nay, xanh = sắp tới), `ox-av` (avatar chữ cái), `ox-dot ok/warn/bad`, `ox-cb` / `ox-cb on` (checkbox), `ox-toggle` / `ox-toggle on`, `ox-mark`, `ox-hl`, chữ `ox-mu` / `ox-ok` / `ox-bad` / `ox-teal` |
| Settings | `ox-settings` (2 cột) > `ox-sh` (tiêu đề nhóm), `ox-set` (`ox-cb` + `div` gồm `.t`, `.d`, `.sub`) |
| Hộp thoại | `ox-dialog` > `.h` (tiêu đề), `.b` (nội dung), `.f` (nút) |

## Mẫu

### Kanban CRM có activity quá hạn (marker 1)

```html
<div class="ox"><div class="ox-nav"><span class="ox-app">CRM</span><span>Sales</span><span>Leads</span><span>Reporting</span><span>Configuration</span></div>
<div class="ox-cp"><div><span class="ox-btn ox-primary">New</span><span class="ox-bc"><b>Pipeline</b></span></div><div><span class="ox-search"><span class="ox-facet">My Pipeline</span>Search...</span><span class="ox-views"><span class="on">▦</span><span>☰</span><span>▤</span></span></div></div>
<div class="ox-kanban"><div class="ox-col"><div class="ox-colh">New <small>$ 24,000</small></div><div class="ox-prog"><i class="g" style="width:40%"></i><i class="o" style="width:20%"></i><i class="r" style="width:30%"></i><i class="x" style="width:10%"></i></div>
<div class="ox-card"><div class="t">Office furniture</div><div class="s">Deco Addict</div><div><span class="ox-tag c2">Product</span><span class="ox-tag c5">Design</span></div><div class="foot"><span><span class="ox-stars"><b>★★</b>★</span><span class="ox-act late"></span><span class="ox-mark">1</span></span><span class="ox-av">MA</span></div></div></div>
<div class="ox-col"><div class="ox-colh">Qualified <small>$ 9,500</small></div><div class="ox-prog"><i class="g" style="width:100%"></i></div><div class="ox-card"><div class="t">Quote for 12 tables</div><div class="s">Gemini Furniture</div><div class="foot"><span><span class="ox-stars"><b>★</b>★★</span><span class="ox-act planned"></span></span><span class="ox-av">AD</span></div></div></div></div></div>
```

### Form báo giá: statusbar, smart button, ribbon, tab (marker 2)

```html
<div class="ox"><div class="ox-cp"><div><span class="ox-btn ox-primary">New</span><span class="ox-bc"><a>Quotations</a> / <b>S00042</b></span></div><div><span class="ox-pager">1 / 12</span></div></div>
<div class="ox-body"><div class="ox-bar"><div><span class="ox-btn ox-primary">Send by Email</span><span class="ox-btn">Confirm</span><span class="ox-btn">Preview</span><span class="ox-btn">Cancel</span></div><div class="ox-status"><span class="on">Quotation</span><span>Quotation Sent</span><span>Sales Order</span></div></div>
<div class="ox-sheet"><div class="ox-smarts"><div class="ox-smart"><b>1</b>Delivery</div><div class="ox-smart"><b>0</b>Invoices</div></div><div class="ox-ribbon ok">Paid</div><div class="ox-title"><small>Quotation</small>S00042</div>
<div class="ox-fields"><div><div class="ox-f"><span class="l">Customer</span><span class="v req">Deco Addict</span></div><div class="ox-f"><span class="l">Invoice Address</span><span class="v">Deco Addict</span></div></div><div><div class="ox-f"><span class="l">Expiration</span><span class="v">12/31/2026</span></div><div class="ox-f"><span class="l">Pricelist <span class="ox-mark">2</span></span><span class="v">Public Pricelist (USD)</span></div></div></div>
<div class="ox-tabs"><span class="on">Order Lines</span><span>Optional Products</span><span>Other Info</span></div>
<table class="ox-list"><thead><tr><th>Product</th><th class="n">Quantity</th><th class="n">Unit Price</th><th class="n">Amount</th></tr></thead><tbody><tr><td>[FURN_7800] Desk Combination</td><td class="n">2.00</td><td class="n">450.00</td><td class="n">$ 900.00</td></tr></tbody></table></div></div></div>
```

### Trang Settings (marker 3)

```html
<div class="ox"><div class="ox-settings"><div class="ox-sh">Pricing</div><div class="ox-set"><span class="ox-cb on"></span><div><div class="t">Discounts</div><div class="d">Grant discounts on sales order lines</div></div></div><div class="ox-set"><span class="ox-cb"></span><div><div class="t">Pricelists <span class="ox-mark">3</span></div><div class="d">Set multiple prices per product, automated discounts, etc.</div><div class="sub"><span class="ox-btn ox-link">→ Pricelists</span></div></div></div></div></div>
```
