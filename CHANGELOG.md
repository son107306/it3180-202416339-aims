# Changelog

Các phiên bản theo [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) và Semantic Versioning.

## [Unreleased]

### Added
- Khôi phục mã AIMS-mini qua các PR bổ sung ngày 2026-11-14.
- Lab 01–03: DVD model, Cart, in giỏ hàng, tìm theo tiêu đề, giảm giá, regression test và use-case.
- Quy trình PR, CI và ghi nhận xung đột/hủy thay đổi.

### Fixed
- Điều kiện giới hạn 20 DVD — Issue #10, PR #11.
- Công thức tính giá sau giảm — PR #12.

## [1.1.0] - 2026-11-09 (tag lịch sử)

**Cảnh báo kiểm toán:** tag đã có trước khi khôi phục chương trình. Bản theo tag hiện tại **không** chứa mã AIMS-mini hoàn chỉnh hay test như yêu cầu. Không dùng tag này để khẳng định đã đạt checklist Lab 05.

## [1.0.1] - 2026-11-09 (nhánh lịch sử release/lab04)

### Fixed
- Search không phân biệt chữ hoa/thường (PR #2).

**Cảnh báo:** Chưa tồn tại tag `v1.0.1`; phiên bản trên nhánh cũ vẫn thiếu chương trình và test.

## [1.0.0] - 2026-11-09 (tag lịch sử)

### Added
- Khởi tạo cấu trúc repository và nhánh refactor.

**Cảnh báo kiểm toán:** `main.py` trong tag `v1.0.0` là tệp rỗng. Tag không đại diện cho một bản ứng dụng đạt kiểm thử.

## Ghi chú phát hành bổ sung

Không di chuyển hoặc thay thế tag `v1.0.0`, `v1.1.0` đã chia sẻ. Khi sửa các dòng phát hành, dùng tag PATCH mới tại commit đạt kiểm thử và chỉ công bố GitHub Release sau khi xác nhận.
