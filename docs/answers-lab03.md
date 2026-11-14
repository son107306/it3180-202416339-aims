# Lab 03 — Bugfix, conflict & undo flow

## Câu hỏi thảo luận

**Merge base là gì?** Đây là tổ tiên chung gần nhất (hoặc các tổ tiên chung tốt nhất) của hai commit/nhánh. Git dựa vào merge base để tính hai chuỗi thay đổi tương ứng, từ đó có thể phát hiện xung đột khi cả hai nhánh sửa một vùng mã nguồn giống nhau.

**Vì sao `master` và `release/*` phải dùng revert?** Đây là lịch sử đã chia sẻ cho người khác và dùng để xác định baseline. `git revert` tạo commit mới thực hiện thay đổi ngược lại nhưng vẫn giữ nguyên SHA các commit gốc, giúp audit và đảm bảo người khác có thể pull an toàn. `reset` hoặc rebase trên nhánh chung có thể gây mất commit hoặc buộc force-push.

**Khi nào dùng `git reset --soft`, `--mixed`, `--hard`?** Soft dời HEAD nhưng giữ staging; mixed bỏ staging và giữ thay đổi ở working directory; hard đồng bộ cả HEAD/index/working directory, làm mất thay đổi chưa lưu. Chỉ thực hành trên nhánh nháp chưa chia sẻ.

**`git reflog` cứu được gì?** Reflog lưu vị trí HEAD/nhánh gần đây trong repo local. Có thể dùng SHA trong đó để khôi phục commit không còn được ref nào trỏ tới sau reset. Reflog là cục bộ, không đồng bộ qua GitHub.

## Bằng chứng thực tế trong repository

- Issue #10 → PR #11: commit regression test trước commit fix; `Fixes #10` làm Issue tự đóng khi merge vào master.
- PR #12: bugfix vào base `feature/discount`, sau đó PR #13 mới tích hợp feature vào master.
- PR #14 và #15: hai feature branch cùng sửa đoạn thông báo sau `self.items.append(dvd)`. Sau khi PR #14 merge, #15 xảy ra conflict; merge commit `d97ab03` có hai parent đã kết hợp tiếng Việt và tên DVD.
- PR #16: một commit đảo ngược hành vi thêm tiêu đề trong thông báo và merge qua PR. Đây là hoàn tác tương đương về **hành vi**, không phải bằng chứng chạy lệnh `git revert -m 1`.

## Các bước chỉ kiểm chứng được tại máy local

```bash
git switch -c topic/undo-practice
# tạo một commit thử nghiệm KHÔNG push
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git reflog
```

Các lệnh trên là hướng dẫn để người nộp tự thực hiện. Không thể chứng minh bằng lịch sử remote khi chưa có log/screenshot từ máy.
