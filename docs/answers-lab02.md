# Lab 02 - Feature/topic, PR và review

## Vì sao đồng bộ master trước PR?
Nhận thay đổi mới, phát hiện xung đột và chạy test tích hợp sớm. feature/search-by-title tạo từ master trước cart-print, sau đó fetch và merge origin/master, chạy demo rồi gửi PR #4.

## Khi nào không được rebase?
Không rebase master/release hoặc commit đã chia sẻ mà người khác đang dùng. Rebase đổi SHA. Bài thực hành rebase conflict dùng nhánh mới chưa push, không viết lại lịch sử chung.

## feature khác topic thế nào?
feature phục vụ chức năng sản phẩm; topic phục vụ công việc như tài liệu, cấu hình, chuẩn bị phát hành. Cả hai tạo từ master và tích hợp qua PR.

## So sánh ba kiểu merge
Merge commit giữ các commit và cấu trúc nhánh; squash gom thay đổi thành một commit; rebase tạo SHA mới trên nền mới và lịch sử tuyến tính. PR #3 dùng merge, #4 squash, #5 rebase. Revert một merge dùng -m để chọn mainline; squash thường revert một commit; rebase nhiều commit có thể cần revert nhiều lần.

## Review
PR #3 được mở trước commit xử lý giỏ rỗng 2b9a540, sau đó cập nhật cùng nhánh. Chưa có partner nên không có Request changes/Approve độc lập. Dùng chế độ cá nhân 0 approval mà tài liệu cho phép. Không đánh dấu vòng review partner là hoàn thành.
