# Báo cáo hoàn thiện IT3180 — Nguyễn Văn Sơn (202416339)

## Minh chứng GitHub

- Lab 01: PR #4 (khôi phục DVD/Cart/main/test), #5 (Lab 01 answers/PR template); release/lab01.
- Lab 02: PR #5–9, merge/squash/rebase; release/lab02.
- Lab 03: Issue #10 → PR #11, PR #12 base feature/discount rồi #13 base master; PR #14–15 conflict với merge commit có hai parent; PR #16 hành vi đảo ngược; release/lab03.
- Lab 04: PR #18 cập nhật CHANGELOG và audit, PR #19 thêm sorting, #21 sửa baseline release/lab04.
- Lab 05: PR #20 tìm theo thể loại, GitHub Actions CI, release/lab05 cần kiểm toán riêng.

## Những bước chưa thể tự xác nhận

- Changes requested → Approved phải do reviewer khác ghi nhận.
- Branch protection và status check bắt buộc cần được cấu hình thủ công.
- SSH, reset, reflog, amend và cherry-pick -x cần minh chứng từ máy local.
- Tags v1.0.0 và v1.1.0 công bố trước khôi phục code, vẫn là snapshots lịch sử chưa đạt test. Không rewrite.

## Chạy thử

```bash
python main.py
python -m unittest discover -s tests -v
```
