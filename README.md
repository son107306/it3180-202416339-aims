# AIMS-mini — IT3180

Ứng dụng Python nhỏ cho chuỗi bài thực hành **Quản lý cấu hình phần mềm với Git/GitHub**, mã học phần IT3180.

- Sinh viên: Nguyễn Văn Sơn
- MSSV: 202416339
- Repository: https://github.com/son107306/it3180-202416339-aims

## Yêu cầu và chạy thử

- Python >= 3.10; không cần cài thư viện bên ngoài.
- Chạy chương trình: `python main.py` — dự kiến `Total cost: 63.89 $`.
- Kiểm thử: `python -m unittest discover -s tests -v`.

## Quy trình nhánh

Tạo nhánh ngắn `refactor/*`, `feature/*`, `topic/*`, `bugfix/*` từ `master`, mở Pull Request vào `master` và để CI kiểm tra. `release/labXX` là các baseline nộp bài; hotfix tạo từ nhánh release bị ảnh hưởng. Không thay đổi các tag đã phát hành.

## Tài liệu

- Câu trả lời: `docs/answers-lab01.md` … `docs/answers-lab05.md`.
- Sơ đồ: `docs/use-case.md`.
- Lịch sử: `CHANGELOG.md`.
- Các giới hạn xác thực lịch sử xem `docs/audit-status.md` (khi được bổ sung).
