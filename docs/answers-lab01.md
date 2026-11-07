# Lab 01 - Cau tra loi

## global va local
`--global` luu cau hinh nguoi dung trong ~/.gitconfig (hoac XDG config); `--local` luu trong .git/config cua repository. Cau hinh local uu tien hon global.

## Vi sao git mv?
Lenh the hien ro y dinh di chuyen, dong thoi stage duong dan cu va moi. Git nhan dien rename theo do tuong dong noi dung, khong luu mot metadata rename rieng. `git log --follow -- aims/cart.py` theo doi lich su qua rename.

## release/lab01 co phai baseline?
Co: day la moc bai nop da thong nhat. Nhanh co the di chuyen khi sua qua hotfix; tag se dinh danh bat bien mot commit khi duoc tao o Lab 04.

## Vi sao van dung PR khi lam mot minh?
PR ghi lai muc dich, diff va cach kiem thu, tao diem kiem soat truoc khi tich hop. Che do mot minh dat approvals = 0; khong gia lap partner approval.

## Bang chung thuc hanh
Da thu restore, restore --staged va amend tren commit chua push. main.py truoc va sau refactor deu in Total cost: 63.89 $. Khong commit cache Python.
