# Lab 04 - Cau tra loi

## Vi sao chuan bi tren master?
Version va CHANGELOG la thay doi can review, tich hop vao dong phat trien truoc khi tach baseline. Khong commit truc tiep tren release.

## Vi sao khong merge release vao master?
Release la dong bao tri: co version/changelog rieng. Merge ca nhanh co the dua metadata phien ban cu vao master. Chi chuyen ban sua can thiet qua cherry-pick -x va PR.

## So sanh GitFlow
GitFlow co develop, feature, release, hotfix va dong bo ve cac nhanh dai han. Release Flow cua hoc phan dung master de tich hop va release/labXX lam baseline tung bai; release khong merge nguoc vao master.

## Vi sao 1.0.0 thay vi 0.4.0?
0.y.z danh dau giai doan chua on dinh. Moc 1.0.0 the hien quyet dinh cong bo API/on dinh theo bai, khong phai bat buoc do day la lab thu tu. MINOR them tinh nang tuong thich; PATCH sua loi; MAJOR pha vo tuong thich.

## Tag va nhanh
Annotated tag dinh danh mot baseline va luu thong tin tagger/message; khong doi tag da chia se. release/lab04 co the nhan hotfix qua PR. A..B la commit co trong B nhung khong trong A; cherry-pick tao SHA moi nen can kiem tra patch-equivalence va hanh vi.
