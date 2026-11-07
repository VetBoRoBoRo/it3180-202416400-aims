# Lab 03 - Bugfix, conflict và hoàn tác

## Merge base là gì?
Là tổ tiên chung tốt nhất của hai commit. Merge ba chiều đối chiếu hai phía với tổ tiên chung để kết hợp thay đổi. Hai nhánh sửa cùng dòng print trong cart.py đã tạo conflict thật.

## Vì sao master/release dùng revert?
Revert thêm commit đảo ngược, giữ SHA và lịch sử đã chia sẻ. Reset/rebase thay lịch sử và có thể ảnh hưởng người đang dựa trên commit cũ. Revert merge cần -m 1 để chọn parent master làm mainline.

## Bằng chứng bugfix
Issue #6 -> test 9609b3b FAIL (True is not false) -> fix f375b4e PASS -> PR #7 với Fixes #6 -> Issue đóng. Bugfix giảm giá trong clone aims-dev2 có test FAIL trước fix; PR #8 có base feature/discount, rồi PR #9 mới tích hợp feature vào master. 100 giảm 20% còn 80; 150% gây ValueError.

## Conflict và rebase
PR #10 đổi thông báo tiếng Việt vào trước. PR #11 sửa cùng dòng và conflict; commit da20e86 kết hợp tiếng Việt + tên DVD sau khi chạy 4 tests. Nhánh riêng topic/rebase-practice tái hiện cùng conflict và hoàn thành rebase --continue. PR #12 dùng revert -m 1 để hoàn tác merge PR #11, giữ thông báo của PR #10.

## Reset và reflog
topic/undo-practice không push: soft đưa thay đổi về staging, mixed về working directory. Hard reset chỉ bỏ empty commit, không xóa nội dung file người dùng. reflog tìm lại commit và topic/reflog-recovered giữ tham chiếu khôi phục. Các nhánh thực hành được giữ lại.

## Bảo trì sau nộp
Phát hiện lỗi mã hóa dấu tiếng Việt do pipeline PowerShell; PR #24 sửa release/lab03 qua hotfix. Tag v0.3.0 gốc không bị di chuyển.
