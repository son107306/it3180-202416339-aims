# Lab 02 — Feature/Topic flow và Pull Request

## Câu hỏi thảo luận

### Vì sao cần đồng bộ `master` trước khi gửi PR?

Trong thời gian phát triển, người khác có thể đã merge thay đổi lên `master`. `git fetch origin` và `git merge origin/master` (hoặc rebase nếu nhánh chưa chia sẻ) cho phép giải quyết xung đột sớm và kiểm thử kết quả tích hợp trước khi đề nghị hợp nhất. Đồng bộ không thay thế kiểm tra CI hay review.

### Khi nào không được rebase?

Không rebase những commit đã chia sẻ và đang được người khác dựa vào, đặc biệt commit trên `master` và `release/*`. Rebase thay đổi SHA và dễ làm mất lịch sử đã được đồng thuận. Với nhánh cá nhân chưa chia sẻ, rebase có thể dùng để làm gọn lịch sử.

### `feature/*` khác `topic/*` như thế nào?

`feature/*` dùng cho thay đổi hành vi sản phẩm (chẳng hạn `Cart.print_cart`); `topic/*` dùng cho chủ đề hỗ trợ như tài liệu, PR template hoặc use-case. Cả hai thường tạo từ `master`, có phạm vi ngắn và hợp nhất bằng PR.

### Ba kiểu merge khác nhau ra sao?

| Cách merge | Lịch sử | Ưu điểm | Lưu ý |
| --- | --- | --- | --- |
| Merge commit | Giữ commit nhánh và thêm merge commit | Truy vết quá trình review, thay đổi từng bước | Lịch sử không tuyến tính |
| Squash and merge | Gộp thành một commit trên base | Dễ revert cả feature | Mất chi tiết các commit riêng trên base |
| Rebase and merge | Phát lại commit trên đầu base, SHA mới | Tuyến tính, vẫn có commit riêng | Không nên rebase nhánh chung đã chia sẻ |

## Ghi nhận bằng chứng

- PR #5: thêm template và câu trả lời Lab 01 (squash).
- PR #6: tính năng hiển thị giỏ hàng (merge commit).
- PR #7: tìm kiếm theo tiêu đề và test (squash).
- PR #8: sơ đồ use-case (rebase).
- PR của tệp này: tài liệu thảo luận (merge).

Những PR này là hoạt động bổ sung thực tế vào ngày sửa bài, không phải PR cũ của buổi thực hành. Bằng chứng yêu cầu "Changes requested → Approved" cần một reviewer khác và không thể được tái tạo bằng tài liệu.
