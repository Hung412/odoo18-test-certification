# Odoo 18 Functional Certification – Đề thi thử

12 đề thi thử chứng chỉ **Odoo 18 Functional Certification**: 3 đề đầy đủ mô phỏng đúng thể lệ kỳ thi thật, và 9 đề rút gọn 45 phút để luyện nhanh (từ Đề 7 có câu hỏi kèm hình ảnh giao diện, như đề thật). Sau khi nộp bài, trang hiện thống kê đúng/sai và lời giải thích cho từng câu.

Toàn bộ nằm trong một file HTML tĩnh duy nhất ([`Odoo18_Mock_Certification.html`](Odoo18_Mock_Certification.html)): không cần server, không cần cài đặt gì.

## Làm bài

**Online (GitHub Pages):** <https://hung412.github.io/odoo18-test-certification/Odoo18_Mock_Certification.html>

> Link chỉ chạy khi repo đã bật GitHub Pages (xem [Triển khai GitHub Pages](#triển-khai-github-pages)).

**Trên máy:** tải file `Odoo18_Mock_Certification.html` về rồi mở bằng trình duyệt (Chrome, Edge, Firefox, Safari).

```bash
git clone https://github.com/Hung412/odoo18-test-certification.git
xdg-open odoo18-test-certification/Odoo18_Mock_Certification.html   # macOS: open, Windows: start
```

> Lưu ý: GitHub chỉ hiển thị mã nguồn của file `.html`, không chạy trang. Muốn làm bài trên web thì dùng link GitHub Pages ở trên.

## Thể lệ

| | Đề đầy đủ (Đề 1–3) | Đề rút gọn (Đề 4–12) |
|---|---|---|
| Số câu | 125 câu | 63 câu |
| Thời gian | 90 phút | 45 phút |
| Điểm đạt | **≥ 70%**: 87,5 / 125 điểm | **≥ 70%**: 44,1 / 63 điểm |
| Trả lời đúng | **+1** điểm | **+1** điểm |
| Trả lời sai | **−0,5** điểm | **−0,5** điểm |
| Bỏ trống | **0** điểm | **0** điểm |

Đề đầy đủ giống hệt thể lệ đề thật. Đề rút gọn giảm một nửa số câu, thời gian và số điểm cần đạt (125 câu được làm tròn lên thành 63), nên tỉ lệ đạt vẫn là 70%. Mỗi câu chỉ có 1 đáp án đúng; hết giờ, bài tự động nộp.

Câu hỏi và đáp án viết bằng **tiếng Anh** như đề thật; giao diện và lời giải thích bằng **tiếng Việt**.

## Nội dung đề

3 đề × 125 câu + 9 đề × 63 câu = **942 câu**, không câu nào lặp lại giữa 12 đề. Câu của đề rút gọn được soạn mới, không lấy từ đề đầy đủ. Mỗi đề có đủ 16 phân hệ thuộc phạm vi thi:

| Phân hệ | Đề đầy đủ | Đề rút gọn | Phân hệ | Đề đầy đủ | Đề rút gọn |
|---|---:|---:|---|---:|---:|
| Accounting | 10 | 5 | Marketing | 8 | 4 |
| Inventory | 10 | 5 | Point of Sale | 8 | 4 |
| Sales | 9 | 5 | Website | 7 | 4 |
| Studio | 9 | 5 | eCommerce | 7 | 3 |
| CRM | 8 | 4 | Project | 7 | 3 |
| Purchase | 8 | 4 | Timesheets | 6 | 3 |
| Manufacturing | 8 | 4 | Survey | 6 | 3 |
| HR | 8 | 4 | Spreadsheet | 6 | 3 |
| | | | **Tổng / đề** | **125** | **63** |

**Câu hỏi có hình (Đề 7–12):** Đề 7–9 có 12 câu, Đề 10–12 có 15 câu kèm hình giao diện Odoo 18, ví dụ kanban CRM, form hóa đơn, statusbar, danh sách, trang Settings, màn hình POS. Câu hỏi thường trỏ vào một vị trí được đánh số trên hình ("marker 1"). Hình được vẽ lại bằng HTML/CSS theo giao diện Odoo 18 với dữ liệu demo (không phải ảnh chụp thật), nên vẫn nằm gọn trong một file HTML. Từ Đề 10, mỗi hình được vẽ theo đúng view XML của Odoo 18 (nút trên header, trạng thái statusbar, nhãn trường, tab, smart button).

**Độ dài đáp án:** các lựa chọn được viết với độ dài và mức chi tiết tương đương nhau. Đáp án đúng chỉ là lựa chọn dài nhất ở khoảng 10–23% số câu và ngắn nhất ở khoảng 20–30%, nên mẹo "chọn câu dài nhất" không còn tác dụng. Tỉ lệ từng đề được in ra mỗi lần chạy `python3 build.py`.

## Tính năng

**Trong khi làm bài**
- Đồng hồ đếm ngược, thanh tiến độ, bảng lưới các câu để nhảy nhanh tới câu bất kỳ.
- Đánh dấu câu cần xem lại; nút *Xóa lựa chọn* để bỏ trống câu chưa chắc (bỏ trống không bị trừ điểm).
- Tùy chọn xáo trộn thứ tự câu hỏi và đáp án.
- Phím tắt: `A`–`D` chọn đáp án · `←` `→` chuyển câu · `F` đánh dấu · `Del` xóa lựa chọn.
- Lỡ tải lại trang vẫn làm tiếp được, thời gian vẫn tiếp tục chạy.

**Sau khi nộp bài**
- Điểm, cách tính điểm, kết quả **Đạt / Chưa đạt**, số câu đúng / sai / bỏ trống và thời gian đã dùng.
- Bảng thống kê theo từng phân hệ và gợi ý 3 phân hệ nên ôn thêm.
- Xem lại từng câu: đáp án bạn chọn, đáp án đúng, giải thích và link tài liệu Odoo 18. Lọc được theo câu sai, câu bỏ trống, câu đã đánh dấu hoặc theo phân hệ.
- Điểm cao nhất của từng đề hiện ngay trên trang chọn đề.

**Lịch sử làm bài**
- Mỗi lần nộp bài (kể cả khi hết giờ, tự nộp), kết quả tự lưu vào trang **Lịch sử làm bài**, mở từ nút trên trang chọn đề hoặc trang kết quả.
- Mỗi lần thi có: thời điểm nộp, đề, điểm, tỉ lệ, Đạt / Chưa đạt, số câu đúng / sai / bỏ trống, thời gian làm. Lọc được theo đề, kèm số lần thi, số lần đạt, điểm trung bình và điểm cao nhất.
- Bấm **Xem lại** để mở lại đúng trang kết quả của lần thi đó: thống kê theo phân hệ, đáp án đã chọn (đúng thứ tự đáp án lúc làm), câu đã đánh dấu, giải thích.
- Xóa được từng lần thi hoặc toàn bộ lịch sử.
- Giữ tối đa 300 lần thi; 150 lần gần nhất xem lại được chi tiết từng câu.

Tiến độ và lịch sử chỉ lưu trong `localStorage` của trình duyệt đang dùng, không gửi đi đâu. Vì vậy lịch sử không đồng bộ giữa các máy hay trình duyệt, và sẽ mất khi xóa dữ liệu trình duyệt hoặc dùng cửa sổ ẩn danh.

**Đối chiếu tài liệu:** câu hỏi được kiểm tra với bộ tài liệu chính thức Odoo 18.0 ([odoo/documentation](https://github.com/odoo/documentation/tree/18.0), nhánh 18.0) và mã nguồn Odoo 18. Khi hai nguồn nói khác nhau, đề theo mã nguồn, vì đó là hành vi thật của bản 18.0. Đề 10–12 còn được một lượt soát chéo độc lập kiểm lại từng câu và từng hình. Mọi link "Tài liệu Odoo 18" trong phần giải thích đều trỏ tới trang có thật của docs 18.0.

## Cấu trúc repo và cách sửa đề

```
data/set1.json … set9.json   # câu hỏi của từng đề (nguồn chính)
src/template.html            # giao diện + logic trang thi
build.py                     # ghép data + template -> Odoo18_Mock_Certification.html
docs/ui-kit.md               # bộ khung vẽ giao diện Odoo cho câu hỏi có hình
tools/preview_images.py      # chụp ảnh xem trước các câu có hình (cần google-chrome)
tools/check_refs.py          # kiểm tra link tài liệu trong data/ có tồn tại trong docs 18.0
```

`Odoo18_Mock_Certification.html` là file được sinh ra. Muốn sửa câu hỏi hay giao diện thì sửa `data/` hoặc `src/`, rồi chạy:

```bash
python3 build.py
```

Lệnh này kiểm tra dữ liệu (đủ 4 đáp án khác nhau, `answer` từ 0–3, không trùng câu), in thống kê từng đề, rồi ghi lại file HTML. Chạy `python3 build.py --check` nếu chỉ muốn kiểm tra mà không ghi file.

Mỗi câu hỏi trong `data/setN.json` có dạng:

```json
{
 "subject": "Inventory",
 "question": "…",
 "options": ["…", "…", "…", "…"],
 "answer": 2,
 "explanation": "Giải thích bằng tiếng Việt…",
 "ref": "https://www.odoo.com/documentation/18.0/…",
 "image": "<div class=\"ox\">…</div>"
}
```

Kiểm tra link tài liệu (cần bản sao repo docs nhánh 18.0):

```bash
git clone --depth 1 --branch 18.0 https://github.com/odoo/documentation.git ../odoo-docs-18
python3 tools/check_refs.py ../odoo-docs-18
```

`answer` là vị trí đáp án đúng, tính từ 0. Trường `image` chỉ có ở câu có hình; cách vẽ xem [docs/ui-kit.md](docs/ui-kit.md). Lịch sử làm bài nhận diện câu hỏi theo nội dung câu hỏi, nên sửa đáp án hay giải thích không ảnh hưởng lịch sử cũ. Riêng khi sửa lời câu hỏi, câu đó sẽ không còn hiện trong phần xem lại của các lần thi trước.

## Triển khai GitHub Pages

1. Vào **Settings ‣ Pages** của repo.
2. Ở **Build and deployment**, chọn *Source*: **Deploy from a branch**, *Branch*: **main**, thư mục **/ (root)**, rồi bấm **Save**.
3. Sau khoảng 1 phút, trang chạy tại link ở mục [Làm bài](#làm-bài).

GitHub Pages cho repo **private** cần gói GitHub Pro / Team / Enterprise. Với tài khoản Free thì repo phải ở chế độ **public**.

## Nguồn tham khảo

- Tài liệu chính thức Odoo 18.0: <https://www.odoo.com/documentation/18.0/>
- Khóa học eLearning Odoo: <https://www.odoo.com/slides>

## Lưu ý

Đây là đề **tự soạn để luyện tập**, không phải đề thi chính thức và không liên kết với Odoo S.A. Câu hỏi được đối chiếu với tài liệu và mã nguồn Odoo 18. Riêng một số tính năng Enterprise (Shop Floor, MPS, PLM/ECO, Quality, Preparation Display, Peppol) được soạn theo hiểu biết, nên có thể có câu chưa khớp hoàn toàn với bản 18.0. Nếu thấy câu nào sai, hãy mở issue.
