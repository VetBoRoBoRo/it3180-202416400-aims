# Báo cáo thực hành Git/GitHub IT3180

Ngày thực hiện: 07/11/2026. MSSV: **202416400**.
Repository: https://github.com/VietTran06/it3180-202416400-aims
Nguồn yêu cầu: IT3180_0504_C5.4-Thuc-hanh-Git-GitHub.pdf, các trang 11-64.

## 1. Phạm vi và trạng thái

Đã thực hiện tuần tự 5 lab trên cùng repo, có commit trung gian thật, Issue/PR thật, ba kiểu merge, conflict/revert, baseline/tag, hotfix đa phiên bản và CI. Báo cáo và câu trả lời được đưa vào qua PR.

Bài làm dùng chế độ cá nhân (0 approval) theo trang 13/29. **Chưa có partner thực hiện Request changes/Approve**. Không coi commit tự sửa là review độc lập. Mọi nhánh đã merge được giữ lại theo yêu cầu không xóa; bước Delete branch trong checklist chưa thực hiện. Không nộp LMS thay người dùng.

## 2. Môi trường và thiết lập

- Git 2.48.1.windows.1; Python cục bộ 3.13.9; CI Python 3.12; không cần pip dependencies.
- Giữ nguyên thông tin tác giả Git đã cấu hình. main gốc được giữ lại; master tạo từ commit 898b62b và đặt làm default trên GitHub.
- .gitignore loại cache/venv/VS Code; .gitattributes chuẩn hóa LF cho mã/tài liệu/YAML.
- Đã kiểm chứng push trực tiếp master bị GH006: Changes must be made through a pull request.
- master bắt buộc PR + check test, strict up-to-date, enforce admins; 0 approval vì làm một mình.
- Ruleset Protect lab release baselines áp dụng release/*, bắt buộc PR, không bypass, chặn force push và xóa.
- SSH xác thực thành công: Hi VietTran06/it3180-202416400-aims! You've successfully authenticated.
- Dùng deploy key có quyền ghi **chỉ repo này**, đăng ký tại repository Settings > Deploy keys. API key cấp tài khoản trả 404 nên không thực hiện đúng vị trí Settings > SSH and GPG keys trong slide. Không có phiên trình duyệt được kết nối để thực hiện bước cấp tài khoản.
- Key riêng tại ~/.ssh/id_ed25519_it3180_202416400; public key là file cùng tên có đuôi .pub. Private key không đưa vào repo/báo cáo. Host key lấy qua GitHub meta API bằng HTTPS và kiểm tra StrictHostKeyChecking.
- origin dùng SSH; core.sshCommand chỉ cấu hình cục bộ repo. Clone Dev 2 ở ../aims-dev2 vẫn có remote HTTPS; đã dùng thực tế cho bugfix nhánh feature.

## 3. Đối chiếu từng lab

| Lab | Việc đã thực hiện | Bằng chứng chính |
|---|---|---|
| 01 (tr.16-26) | Bootstrap, demo 63.89, restore/staged/amend, git mv, refactor PR, release/lab01 | PR #1; rename 100%; v0.1.0 |
| 02 (tr.27-35) | Protection, PR template, cart print, title search, use case, đồng bộ master, 3 kiểu merge | PR #2-5; #3 merge, #4 squash, #5 rebase; thiếu partner review |
| 03 (tr.36-43) | Issue, test FAIL trước fix, bugfix base feature, Dev2, conflict merge/rebase, reset/reflog, revert PR | Issue #6; PR #7-12; 4 tests |
| 04 (tr.44-52) | Version/CHANGELOG, annotated tags, GitHub Release, phát triển sau baseline, audit, detached HEAD/worktree/ZIP | PR #13-14; v1.0.0; 4 tests baseline/6 tests sau sort |
| 05 (tr.53-64) | Category, 1.1.0, tái hiện lỗi cũ, hotfix 2 commits, cherry-pick -x hai dòng, audit đa phiên bản | Issue #17; PR #15-20; v1.0.1/v1.1.0; 5/8 tests |
| CI mở rộng (tr.62) | Workflow, required check, PR cố ý lỗi bị chặn | PR #21; #22 đóng không merge; Actions failure và blocked |
| Bảo trì bổ sung | Sửa mã hóa tiếng Việt qua hotfix, không viết lại tag/lịch sử chung | PR #23-26; v1.0.2/v1.1.1 |

## 4. Commit và thao tác đáng kiểm tra

- 4faac25: git mv dvd.py/cart.py vào aims/, Git nhận rename 100%; acd9263 sửa import.
- restore và restore --staged đã thử trên thay đổi nháp; amend sửa message sai trước push (commit cuối afe09ea).
- 9609b3b: regression test nhận DVD thứ 21 FAIL; f375b4e: đổi > thành >=, test PASS.
- 9dda071: test giảm giá FAIL; 2873dd4: sửa công thức và validate; PR #8 base feature/discount.
- da20e86: merge conflict thật, kết hợp ý đồ tiếng Việt và tên DVD, 4 tests PASS.
- topic/rebase-practice: nhánh riêng chưa push, conflict thật rồi rebase --continue, không force push nhánh chung.
- topic/undo-practice: reset soft/mixed/hard. Hard reset bỏ một empty commit, không xóa nội dung người dùng. topic/reflog-recovered giữ commit lấy lại bằng reflog.
- a1ddca2: git revert -m 1 merge 7497fc7 qua PR #12; không reset lịch sử chung.
- 0ba41514170270159168c4f2fca9d736df057a7e: chỉ sửa search và test; 519d7a0: version 1.0.1 tách riêng.
- 11c3f34 và ae27e79: hai bản cherry-pick -x của fix; git cherry nhận '-' cho fix tương đương, '+' cho bump version riêng dòng 1.0.x.

## 5. Baseline, release và bảo trì

| Bài/dòng | Tag bài yêu cầu | Nhánh nộp hiện tại |
|---|---|---|
| Lab 01 | v0.1.0 | release/lab01, giữ baseline đầu |
| Lab 02 | v0.2.0 | release/lab02, giữ baseline đầu |
| Lab 03 | v0.3.0 | release/lab03 đã nhận hotfix mã hóa qua PR #24 |
| Lab 04 | v1.0.0; bản vá tìm kiếm v1.0.1 | release/lab04 ở v1.0.2 sau hotfix mã hóa |
| Lab 05 | v1.1.0 | release/lab05 ở v1.1.1 sau hotfix mã hóa |

Tất cả tag là annotated, đã push. v1.0.0, v1.0.1, v1.1.0 và hai patch bổ sung có GitHub Release. Tag cũ không di chuyển/xóa; chúng tái hiện đúng trạng thái lúc phát hành, gồm lỗi đã được sửa ở patch sau. Vì có bảo trì nên nhánh release hiện tại có thể khác tag đầu tiên.

Đã chạy lại v0.2.0 bằng detached HEAD; v1.0.0 có worktree ../aims-v1.0.0 và ZIP ../aims-1.0.0.zip. Giữ worktree để kiểm tra, chưa chạy lệnh xóa theo slide vì yêu cầu không xóa file.

## 6. Kết quả kiểm thử và CI

- main.py trước/sau refactor: Total cost: 63.89 $.
- Lab 03: 4 tests pass sau fix, conflict và revert.
- v1.0.0: 4 tests pass trên worktree riêng; không có sort_by_cost.
- v1.0.1: 5 tests pass; v1.1.0/master tại bước kiểm toán: 8 tests pass.
- v1.0.1, v1.1.0, master: tìm lion trong The Lion King đều trả 1 kết quả.
- diff v1.0.0..v1.0.1 đúng 4 file: search.py, test_search.py, __init__.py, CHANGELOG.md.
- Hotfix mã hóa: kiểm tra chính xác stdout tiếng Việt và toàn bộ 4/5/8 tests theo từng dòng đều pass.
- CI tốt đầu tiên: https://github.com/VietTran06/it3180-202416400-aims/actions/runs/42363815499
- CI cố ý lỗi: https://github.com/VietTran06/it3180-202416400-aims/actions/runs/42364437222 (2/8 tests fail).
- Trước khi đóng PR #22, API báo mergeable=true nhưng mergeable_state=blocked: code không conflict nhưng required check thất bại. Không merge PR lỗi.
- CI hotfix mã hóa: https://github.com/VietTran06/it3180-202416400-aims/actions/runs/42366142638 (success).

Không coi unit tests là bằng chứng có partner review hay có CD. Workflow chỉ chạy kiểm thử, không triển khai ứng dụng.

## 7. Tự kiểm tra lại

```powershell
py -X utf8 main.py
py -X utf8 -m unittest discover -s tests -v
git status --short
git log --oneline --graph --all
git log --oneline --follow -- aims/cart.py
git tag -n
git diff --stat v1.0.0 v1.0.1
git cherry -v origin/master origin/release/lab04
git log --all --oneline --grep "cherry picked from commit 0ba41514170270159168c4f2fca9d736df057a7e"
git worktree list
```

Python trên Windows qua pipe có thể mặc định cp1252: dùng -X utf8. Khi switch tag rất nhanh, cache timestamp .pyc có thể giữ module phiên bản trước nếu kích thước file bằng nhau; dùng worktree riêng hoặc -X pycache_prefix=<thu-muc-rieng-moi-phien-ban> khi kiểm toán, không kết luận mã nguồn sai chỉ từ cache cũ.

## 8. Phần còn cần người dùng

1. Nộp link repo lên LMS theo yêu cầu học phần.
2. Nếu giảng viên yêu cầu chế độ cặp đôi, cần partner thật thực hiện review; chưa có Request changes/Approve độc lập. Chế độ hiện tại là cá nhân theo tài liệu.
3. Nếu bắt buộc key cấp tài khoản thay vì deploy key, người dùng thêm file .pub tại GitHub Settings > SSH and GPG keys. SSH repo hiện đã hoạt động.
4. Nếu muốn dọn nhánh/worktree, cần cho phép xóa; hiện giữ toàn bộ theo chỉ dẫn.

## 9. Danh sách PR tại thời điểm chụp

Snapshot chụp trước PR tài liệu cuối; dữ liệu máy đọc nằm ở audit-snapshot.json.

| PR | Base | Trạng thái | Nội dung |
|---|---|---|---|
| [1](https://github.com/VietTran06/it3180-202416400-aims/pull/1) | master | Merged | refactor: apply Release Flow and complete Lab 01 |
| [2](https://github.com/VietTran06/it3180-202416400-aims/pull/2) | master | Merged | docs: add pull request template |
| [3](https://github.com/VietTran06/it3180-202416400-aims/pull/3) | master | Merged | feat: print cart contents in demo |
| [4](https://github.com/VietTran06/it3180-202416400-aims/pull/4) | master | Merged | feat: add title search |
| [5](https://github.com/VietTran06/it3180-202416400-aims/pull/5) | master | Merged | docs: add use case and Lab 02 answers |
| [7](https://github.com/VietTran06/it3180-202416400-aims/pull/7) | master | Merged | fix: reject the 21st DVD in cart |
| [8](https://github.com/VietTran06/it3180-202416400-aims/pull/8) | feature/discount | Merged | fix: correct discount calculation on feature branch |
| [9](https://github.com/VietTran06/it3180-202416400-aims/pull/9) | master | Merged | feat: add validated cart discounts |
| [10](https://github.com/VietTran06/it3180-202416400-aims/pull/10) | master | Merged | feat: use Vietnamese cart messages |
| [11](https://github.com/VietTran06/it3180-202416400-aims/pull/11) | master | Merged | feat: show added DVD title and resolve conflict |
| [12](https://github.com/VietTran06/it3180-202416400-aims/pull/12) | master | Merged | fix: revert added-title merge and document Lab 03 |
| [13](https://github.com/VietTran06/it3180-202416400-aims/pull/13) | master | Merged | chore: prepare AIMS-mini 1.0.0 |
| [14](https://github.com/VietTran06/it3180-202416400-aims/pull/14) | master | Merged | feat: add cart sorting after 1.0.0 release |
| [15](https://github.com/VietTran06/it3180-202416400-aims/pull/15) | master | Merged | feat: add category search for 1.1.0 |
| [16](https://github.com/VietTran06/it3180-202416400-aims/pull/16) | master | Merged | chore: prepare 1.1.0 baseline before hotfix |
| [18](https://github.com/VietTran06/it3180-202416400-aims/pull/18) | release/lab04 | Merged | fix: patch title search in 1.0.1 |
| [19](https://github.com/VietTran06/it3180-202416400-aims/pull/19) | master | Merged | fix: propagate title-search hotfix to master |
| [20](https://github.com/VietTran06/it3180-202416400-aims/pull/20) | release/lab05 | Merged | fix: propagate title-search hotfix to Lab 05 |
| [21](https://github.com/VietTran06/it3180-202416400-aims/pull/21) | master | Merged | ci: run unit tests for master and release PRs |
| [22](https://github.com/VietTran06/it3180-202416400-aims/pull/22) | master | closed | test: demonstrate CI blocking broken total cost |
| [23](https://github.com/VietTran06/it3180-202416400-aims/pull/23) | master | Merged | fix: preserve Vietnamese message encoding on master |
| [24](https://github.com/VietTran06/it3180-202416400-aims/pull/24) | release/lab03 | Merged | fix: preserve Vietnamese message encoding on release/lab03 |
| [25](https://github.com/VietTran06/it3180-202416400-aims/pull/25) | release/lab04 | Merged | fix: preserve Vietnamese message encoding on release/lab04 |
| [26](https://github.com/VietTran06/it3180-202416400-aims/pull/26) | release/lab05 | Merged | fix: preserve Vietnamese message encoding on release/lab05 |
