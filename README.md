# Odoo 18 Functional Certification – Đề thi thử

Bộ 3 đề thi thử chứng chỉ **Odoo 18 Functional Certification**, mô phỏng đúng thể lệ kỳ thi thật. Sau khi nộp bài, trang hiện thống kê đúng/sai và lời giải thích cho từng câu.

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

## Thể lệ (giống đề thật)

| | |
|---|---|
| Số câu | 125 câu trắc nghiệm, mỗi câu 1 đáp án đúng |
| Thời gian | 90 phút. Hết giờ, bài tự động nộp |
| Trả lời đúng | **+1** điểm |
| Trả lời sai | **−0,5** điểm |
| Bỏ trống | **0** điểm |
| Điểm đạt | **≥ 70%** (87,5 / 125 điểm) |

Câu hỏi và đáp án viết bằng **tiếng Anh** như đề thật; giao diện và lời giải thích bằng **tiếng Việt**.

## Nội dung đề

3 đề × 125 câu = **375 câu**. Trong cùng một phân hệ, câu hỏi giữa các đề không trùng nhau. Mỗi đề có đủ 16 phân hệ thuộc phạm vi thi:

| Phân hệ | Số câu / đề | Phân hệ | Số câu / đề |
|---|---:|---|---:|
| Accounting | 10 | Marketing | 8 |
| Inventory | 10 | Point of Sale | 8 |
| Sales | 9 | Website | 7 |
| Studio | 9 | eCommerce | 7 |
| CRM | 8 | Project | 7 |
| Purchase | 8 | Timesheets | 6 |
| Manufacturing | 8 | Survey | 6 |
| HR | 8 | Spreadsheet | 6 |

## Tính năng

**Trong khi làm bài**
- Đồng hồ đếm ngược, thanh tiến độ, bảng lưới 125 câu để nhảy nhanh tới câu bất kỳ.
- Đánh dấu câu cần xem lại; nút *Xóa lựa chọn* để bỏ trống câu chưa chắc (bỏ trống không bị trừ điểm).
- Tùy chọn xáo trộn thứ tự câu hỏi và đáp án.
- Phím tắt: `A`–`D` chọn đáp án · `←` `→` chuyển câu · `F` đánh dấu · `Del` xóa lựa chọn.
- Lỡ tải lại trang vẫn làm tiếp được, thời gian vẫn tiếp tục chạy.

**Sau khi nộp bài**
- Điểm, cách tính điểm, kết quả **Đạt / Chưa đạt**, số câu đúng / sai / bỏ trống và thời gian đã dùng.
- Bảng thống kê theo từng phân hệ và gợi ý 3 phân hệ nên ôn thêm.
- Xem lại từng câu: đáp án bạn chọn, đáp án đúng, giải thích và link tài liệu Odoo 18. Lọc được theo câu sai, câu bỏ trống, câu đã đánh dấu hoặc theo phân hệ.
- Lưu lịch sử và điểm cao nhất của từng đề.

Tiến độ và lịch sử điểm chỉ lưu trong `localStorage` của trình duyệt đang dùng; không gửi đi đâu.

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
