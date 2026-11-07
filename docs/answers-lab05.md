# Lab 05 - Hotfix và CI

## Upstream first và release first
Upstream first sửa master trước rồi backport: giảm nguy cơ quên dòng phát triển nhưng patch có thể phụ thuộc tính năng mới. Release first sửa đúng bản người dùng đang chạy: bản vá nhỏ và tái hiện đúng môi trường, nhưng phải theo dõi lan truyền tới mọi dòng. Học phần yêu cầu release first.

## Phát hiện quên release/lab05 bằng cách nào?
Chạy kiểm tra hành vi trên v1.0.1, v1.1.0 và master: bản thiếu fix sẽ trả 0 thay vì 1 kết quả. log --all --grep nguồn cherry-pick chỉ ra thiếu bản sao, cần đối chiếu nhánh chứa từng commit. tag --contains FIX_SHA chỉ kiểm tra ancestry; git cherry kiểm tra patch-equivalence. Không lệnh nào thay thế hoàn toàn test hành vi.

## Vì sao tách fix và version?
Commit 0ba4151 chỉ sửa search và regression test; 519d7a0 tăng 1.0.1. PR #18 vào release/lab04. PR #19/#20 cherry-pick -x riêng fix, không mang version 1.0.1 đè 1.1.0. Refs #17 trên release giữ Issue mở; Fixes #17 trong PR #19 vào default master đóng Issue.

## Vì sao chưa tag 1.1.0 ngay?
release/lab05 cần nhận fix trước khi tag. Tag đã công bố không đổi; nếu đã tag phải tạo PATCH tiếp theo. v1.1.0 chỉ tạo sau PR #20. File test category được tách bằng git mv trước cherry-pick, tránh add/add và giữ nguyên patch để git cherry nhận diện tương đương.

## Kiểm toán và bảo trì bổ sung
v1.0.1 có 5 tests; v1.1.0 và master lúc kiểm toán có 8 tests; cả ba tìm lion được 1 DVD. diff v1.0.0..v1.0.1 chỉ 4 file. Sau đó hotfix mã hóa tiếng Việt được chuyển bằng PR #23-26; patch v1.0.2 và v1.1.1 giữ nguyên tag cũ.

## CI
PR #21 thêm workflow Python 3.12. Required check test được bật trên master, gồm admin. PR #22 cố ý trả tổng tiền 0 làm 2/8 tests fail; run 42364437222 thất bại và API báo mergeable_state=blocked. PR đã đóng, không merge. Run tốt đầu tiên: 42363815499. Đây là CI kiểm thử, chưa phải pipeline CD triển khai.
