# AIMS-mini - Thực hành Git/GitHub IT3180

MSSV: **202416400**. Ứng dụng CLI Python, chỉ dùng thư viện chuẩn.

## Chạy và kiểm thử

```powershell
py -X utf8 main.py
py -X utf8 -m unittest discover -s tests -v
```

Linux/macOS có thể dùng `python3` thay cho `py`. Yêu cầu Python >= 3.10; CI dùng Python 3.12.
Demo hiện tại in `AIMS-mini v1.1.1`, thông báo tiếng Việt và tổng `63.89 $`. Có 8 unit tests.
`-X utf8` giúp đầu ra tiếng Việt hoạt động khi Windows chuyển hướng stdout qua pipe.

## Tài liệu bài làm

- [Báo cáo nghiệm thu và bằng chứng từng lab](docs/lab-report.md)
- [Ảnh chụp dữ liệu kiểm toán Git/GitHub](docs/audit-snapshot.json)
- [Use case](docs/use-case.md)
- [Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md), [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md), [Lab 05](docs/answers-lab05.md)
- [CHANGELOG](CHANGELOG.md)

## Quy trình

`master` là nhánh tích hợp; bài nộp nằm tại `release/lab01` ... `release/lab05`.
Mọi thay đổi sau bootstrap đều qua PR. master bắt buộc check `test` pass, không bypass bằng quyền admin.
release/* bắt buộc PR và chặn force push/xóa. Chế độ làm một mình dùng 0 approval.
Nhánh `main` khởi tạo và các nhánh đã merge được giữ lại theo yêu cầu không xóa.

## Phiên bản

Tag yêu cầu của bài: v0.1.0, v0.2.0, v0.3.0, v1.0.0, v1.0.1, v1.1.0.
Patch bổ sung v1.0.2 và v1.1.1 sửa mã hóa thông báo tiếng Việt; tag cũ giữ nguyên.
PR #22 là minh chứng CI fail, đã đóng mà không merge.
