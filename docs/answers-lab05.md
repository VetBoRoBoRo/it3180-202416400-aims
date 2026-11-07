# Lab 05 - Cau tra loi

## Upstream first va release first
Upstream first sua tren master truoc roi backport: tranh quen dong phat trien, nhung patch co the phu thuoc tinh nang moi. Release first sua tren release dang bi anh huong: patch toi thieu, test dung ban dang dung, nhung can theo doi lan truyen toi master va cac release khac. Hoc phan yeu cau release first.

## Neu quen release/lab05
Vong kiem tra hanh vi tren v1.0.1, v1.1.0 va master phat hien ban chua sua (ket qua 0 thay vi 1). git log --all --grep nguon cherry-pick cho biet co thieu mot trong hai ban sao; can doi chieu nhanh chua commit do. git tag --contains FIX_SHA chi theo ancestry, khong phat hien patch tuong duong co SHA moi. git cherry kiem tra patch-equivalence, khong thay the test hanh vi.

## Vi sao tach commit fix va version?
Chi cherry-pick fix + regression test, khong dua 1.0.1 de len 1.1.0. Commit -x luu SHA nguon de truy vet. Refs #N tren release khong dong Issue; Fixes #N trong PR vao default master moi dong Issue.

## Vi sao chua tag 1.1.0?
Nhanh release/lab05 can nhan ban sua truoc khi tag. Tag da cong bo khong doi; neu da tag phai phat hanh PATCH tiep theo 1.1.1.

## Lam mot minh
Dung PR, branch protection va approvals=0. Khong co partner review doc lap. CI la phan mo rong, khong phai mot he thong CD trien khai san pham.
