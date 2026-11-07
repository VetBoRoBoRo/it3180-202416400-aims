# Lab 03 - Cau tra loi va bang chung

## Merge base
La to tien chung tot nhat cua hai commit. Merge ba chieu so sanh hai nhanh voi to tien chung de ket hop thay doi. Hai nhanh cung sua dong print trong aims/cart.py gay conflict noi dung.

## Vi sao master/release dung revert?
Revert tao commit dao nguoc, khong doi SHA va lich su da chia se. Reset/rebase doi lich su, co the lam mat lien ket commit va anh huong nguoi khac. Revert merge can -m 1 de chon parent master lam mainline.

## Truy vet loi
Issue #6 -> test 9609b3b (FAIL: True is not false) -> fix f375b4e (PASS) -> PR #7 (Fixes #6). PR #8 co base feature/discount, duoc thuc hien o clone aims-dev2; PR #9 tich hop feature da sua.

## Xung dot
PR #10 vao truoc; PR #11 sua cung dong va gay conflict that. Da ket hop thong bao tieng Viet va ten DVD, chay 4 tests OK, commit da20e86, merge PR #11. Nhanh rieng topic/rebase-practice tai hien conflict bang rebase va da rebase --continue; khong force push lich su chung.

## Hoan tac va khoi phuc
Tren topic/undo-practice (khong push), da thu reset --soft, --mixed va --hard. Hard reset chi bo empty commit, khong xoa noi dung file. Da dung reflog tim empty commit va giu lai bang topic/reflog-recovered. PR nay revert merge PR #11, giu thong bao tieng Viet cua PR #10.

## Kiem thu
4 tests: gioi han 20 DVD, tong tien 63.89, giam 20% cua 100 con 80, tu choi 150%. Tat ca pass sau fix va sau xu ly conflict.
