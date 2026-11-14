# Lab 05 — Hotfix & bảo trì đa phiên bản

## Upstream first so với release first
- **Upstream first:** Sửa đầu tiên ở master, sau đó cherry-pick vào release cũ. Ưu điểm là dòng phát triển chính có fix trước; nhược điểm patch có thể khó áp dụng với code cũ.
- **Release first (học phần):** Sửa từ nhánh release đang lỗi, kiểm thử tại đó, sau đó cherry-pick -x commit sửa vào master và nhánh phát hành khác. Ưu tiên bản đang sử dụng, nhưng phải kiểm tra đủ các dòng bị ảnh hưởng.

## Phát hiện quên đưa fix vào release/lab05
```bash
git cherry -v origin/release/lab05 origin/release/lab04
git log --all --oneline --grep="cherry picked from commit"
git tag --contains <FIX_SHA>
```

Vì cherry-pick tạo SHA mới, `git tag --contains` chỉ theo dõi commit gốc qua ancestry. Kết hợp `git cherry`, trailer `-x` và chạy regression test trên master, release/lab04, release/lab05.

## CI và branch protection
Workflow `.github/workflows/ci.yml` chạy `unittest` trên PR vào master/release và push master. Cấu hình bắt buộc PR/status check `test` phải thực hiện trong Settings → Rulesets hoặc Branch protection. YAML không tự kích hoạt branch protection.

## Giới hạn bằng chứng
Không khẳng định đã chạy `git cherry-pick -x`, tạo tất cả annotated tags hay review/approval nếu GitHub không có commit/tag/sự kiện tương ứng. Cần đối chiếu lệnh thực thi và các ref thật.
