# Lab 01 - Thiết lập và refactor

## --global lưu ở đâu, khác --local thế nào?
Cấu hình người dùng thường nằm ở ~/.gitconfig (hoặc cấu hình XDG). --local nằm trong .git/config của repo và ưu tiên hơn global. Dùng git config --list --show-origin để xem nguồn cấu hình. Bài làm giữ tên/email tác giả đã có, chỉ cấu hình repo khi cần.

## Vì sao dùng git mv?
Lệnh chuyển file và stage đường dẫn cũ/mới, thể hiện rõ ý định refactor. Git phát hiện rename bằng độ tương đồng nội dung; không lưu một thuộc tính rename cố định. git log --follow -- aims/cart.py theo lịch sử qua đổi tên. Commit 4faac25 ghi nhận rename 100%.

## release/lab01 có phải baseline?
Có: đây là trạng thái bài nộp đã thống nhất. Khi vừa tạo, master và release/lab01 cùng commit a1ef28f. Sau đó master phát triển tiếp. Annotated tag v0.1.0 được thêm ở Lab 04 để định danh bất biến baseline này.

## Vì sao làm một mình vẫn dùng PR?
PR lưu mục đích, diff, cách kiểm thử và điểm kiểm soát trước tích hợp. Tài liệu cho phép 0 approval khi làm một mình. Điều này không thay thế bằng chứng review của partner.

## Thực hành
Đã dùng restore để bỏ thay đổi working tree, restore --staged để bỏ staging, amend sửa message trước push. Demo trước/sau refactor đều 63.89 $. SSH được xác thực bằng deploy key chỉ cho repo; chi tiết và khác biệt với key cấp tài khoản nằm trong báo cáo.
