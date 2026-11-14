# Lab 04 — Release flow & versioning

## Vì sao release/* không merge ngược vào master?
Release là baseline riêng, có thể chứa thay đổi về số phiên bản và vá dành riêng cho nhánh bảo trì. Merge toàn bộ release về master có thể mang theo dữ liệu phiên bản cũ. Chỉ lan truyền sửa lỗi cần thiết qua cherry-pick hoặc bản vá tương đương.

## So sánh với GitFlow
IT3180 dùng master làm nhánh tích hợp, feature/topic/bugfix/refactor ngắn hạn, release/labXX từ master và hotfix từ release. GitFlow có thêm nhánh develop dài hạn; feature từ develop, release từ develop, hotfix từ main rồi merge cả main và develop.

## Vì sao 1.0.0 chứ không phải 0.4.0?
Theo SemVer, 1.0.0 thể hiện mốc API được tuyên bố ổn định. 0.x dành cho bản trước ổn định. Đây là quy ước mốc của bài thực hành, không phải đếm số buổi.

## Status accounting & audit
```bash
git log --oneline release/lab04..master
git log --oneline master..release/lab04
git diff --stat v0.3.0 v1.0.0
git describe --tags
git show v1.0.0:aims/__init__.py
git worktree add ../aims-check release/lab04
```

**Lưu ý minh bạch:** PR #21 sửa nhánh release/lab04. Hai tag lịch sử v1.0.0 và v1.1.0 vẫn trỏ tới mã nguồn không hoàn thiện; không được di chuyển các tag đã chia sẻ để che sai sót.
