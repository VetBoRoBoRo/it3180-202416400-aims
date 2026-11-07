# Lab 04 - Release và kiểm toán

## Vì sao chuẩn bị trên master?
Version và CHANGELOG cần review và tích hợp trên dòng phát triển trước khi tách baseline. PR #13 chuẩn bị 1.0.0; không commit trực tiếp lên release.

## Vì sao không merge release về master?
Release có version/changelog riêng của dòng bảo trì. Merge cả nhánh dễ đưa metadata cũ vào master. Cherry-pick -x chỉ bản sửa cần thiết, qua PR, giữ dấu vết SHA gốc.

## So sánh GitFlow
GitFlow dùng develop cùng main, feature, release và hotfix, có bước đồng bộ trở lại các nhánh dài hạn. Flow học phần dùng master để tích hợp, release/labXX để nộp/bảo trì, không merge release về master.

## Vì sao 1.0.0, không phải 0.4.0?
0.y.z thể hiện giai đoạn chưa ổn định. 1.0.0 là quyết định công bố mức ổn định/API theo bài, không phải phép đếm số lab. MINOR thêm tính năng tương thích; PATCH sửa lỗi; MAJOR phá tương thích.

## Tag và branch
Annotated tag lưu thông tin tagger/message và cố định một commit. release/lab04 có thể tiến lên khi nhận hotfix. A..B là commit thuộc B mà không thuộc A. Tag --contains xét ancestry, không nhận diện bản vá tương đương có SHA khác.

## Kiểm toán
v1.0.0 chạy 4 tests trong worktree aims-v1.0.0; ZIP aims-1.0.0.zip tạo bằng git archive. PR #14 thêm sort với 2 tests trên master, v1.0.0 không có sort. Đã chạy log/diff/describe, tái tạo v0.2.0 bằng detached HEAD. Sau bảo trì release/lab04 ở 1.0.2; v1.0.0/v1.0.1 vẫn giữ nguyên.
