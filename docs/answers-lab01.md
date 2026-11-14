# Lab 01 — Thiết lập môi trường và Refactor flow

## Các câu hỏi thảo luận

**1. Vì sao dùng `git mv`?** Lệnh này di chuyển/đổi tên tệp và đưa thay đổi vào staging cùng lúc. Git nhận diện rename chủ yếu bằng mức tương đồng nội dung chứ không lưu một thao tác "rename" riêng. Nhờ giữ nội dung, `git log --follow` có thể truy vết được lịch sử của tệp trước khi chuyển vào `aims/`.

**2. `release/lab01` có phải baseline?** Có. Nhánh này trỏ tới trạng thái mã nguồn đã được lựa chọn để nộp ở Lab 01. Baseline là mốc tham chiếu để so sánh các thay đổi Lab tiếp theo. Một tag như `v0.1.0` còn định danh chính xác một commit bất biến.

**3. Vì sao không commit trực tiếp lên `master` dù làm một mình?** Luồng nhánh → PR → kiểm tra → merge tách thay đổi đang phát triển khỏi baseline tích hợp. PR lưu mục đích, diff, kết quả CI và lịch sử quyết định, đồng thời tạo cơ hội kiểm soát chất lượng trước khi tích hợp.

**4. Git `--global` khác `--local` thế nào?** Cấu hình global nằm trong tệp `~/.gitconfig` (hoặc đường dẫn tương đương theo hệ điều hành), áp dụng cho người dùng trên máy. Local nằm trong `.git/config` của từng repo và ưu tiên hơn global khi cùng khóa cấu hình.

## Thao tác cần minh chứng tại máy cá nhân

- `git status`, `git diff`, `git diff --staged`: đối chiếu working tree, staging và commit.
- `git restore <file>`: bỏ thay đổi chưa stage; `git restore --staged <file>`: đưa file ra khỏi staging.
- `git commit --amend`: chỉ sửa commit chưa chia sẻ.
- `git log --oneline --graph --all` và `git log --follow -- aims/cart.py`: kiểm tra lịch sử.
- `python main.py`: kết quả mong đợi là `Total cost: 63.89 $`.

**Lưu ý về bằng chứng:** Một số bước thao tác tại máy (SSH, restore, amend) không thể kiểm chứng chỉ qua lịch sử GitHub. Không coi tài liệu này là bằng chứng rằng từng lệnh đã được chạy tại máy.
