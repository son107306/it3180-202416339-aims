# Audit of submission history — IT3180

Updated 2026-11-14. This document distinguishes **verified GitHub evidence** from instructions and remaining tasks.

## Gốc đã có trước khi hoàn thiện

- Repository vốn chỉ có 3 PR merged (#1–#3), 5 nhánh gồm master, refactor, hotfix và release/lab04, lab05.
- Hai tag lịch sử `v1.0.0`, `v1.1.0` đã công bố từ 2026-11-09.
- Tại các tag này, `main.py` rỗng và không đạt chương trình mẫu.
- Branch protection cho master chưa bật.

## Hoạt động bổ sung thực tế

| Lab | Bằng chứng |
| --- | --- |
| 01 | PR #4 khôi phục ứng dụng; PR #5 thêm câu trả lời, PR template; `release/lab01` |
| 02 | PR #5–#9; merge commit (#6, #9), squash (#5, #7), rebase (#8); `release/lab02` |
| 03 | Issue #10 → PR #11 (test trước fix); PR #12 base feature/discount → PR #13 master; conflict #14/#15 (merge commit 2 parent); PR #16 đảo ngược thay đổi; `release/lab03` |
| 04 | Xem CHANGELOG và lịch sử tag; baseline cũ phải được kiểm toán trước khi phát hành lại |
| 05 | Xem hướng dẫn hotfix/CI; không khẳng định cherry-pick nếu không có commit minh chứng |

## Chưa thể coi là hoàn thành chỉ bằng cập nhật mã

- Reviewer thật / Changes requested → Approved: cần người khác thực hiện trên GitHub.
- Branch protection/ruleset: cần thao tác ở Settings của chủ repo.
- Các thao tác local Git (SSH, amend/reset/reflog/git mv) cần bằng chứng từ máy người nộp.
- Tag lịch sử có mã không đầy đủ; không được viết lại tag đã phát hành để che lịch sử cũ.

## Kiểm thử

```bash
python main.py
python -m unittest discover -s tests -v
git log --oneline --graph --all
git tag -n
```

Với mỗi PR có CI, tham chiếu trực tiếp mục **Checks / Actions** của PR để xác minh kết quả, không suy từ số commit.
