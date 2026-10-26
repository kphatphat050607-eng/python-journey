# VuaCóc Bot Journey

VuaCóc Bot Journey là project xuyên khóa để người học nâng cấp cùng một hệ
thống ra quyết định từ Week 07 đến Week 15. Game gốc có thể tham khảo tại
[vuacoc.com](https://vuacoc.com/), nhưng track này chỉ dùng mô hình học tập
local, không tuyên bố API/runtime compatibility. Người học không gặp functions,
dict, JSON, exceptions, pytest, modules và OOP như những chương rời rạc:
mỗi chủ đề làm bot **more capable, more reliable, more explainable**.

## 1. Mục tiêu và phạm vi

Capstone tích hợp một bot quyết định, local arena, ba baseline, match replay,
tournament và test. Mục tiêu là tạo một chương trình chạy được, kiểm thử được
và giải thích được — không phải khẳng định bot có chiến thuật tối ưu.

```text
Observe state → Choose action → Run match → Inspect result
                         ↑                         ↓
                      Improve ← Test / Debug ← Replay
```

**Phạm vi được hỗ trợ:** course-local Line Arena, không cần API key, tài khoản
game hoặc kết nối mạng. Kết quả chỉ chứng minh hành vi trong môi trường học tập
local; không chứng minh tương thích với runtime production của VuaCóc.

## 2. Kiến trúc và liên hệ Week 14

```text
Arena → choose_action(state) → Bot → strategy(state)
```

- **Bot** là class nhận một strategy qua phương thức khởi tạo.
- **Bot.choose_action()** ủy quyền quyết định cho strategy đã nhận.
- **balanced_strategy** di chuyển về goal; **defensive_strategy** chờ nếu đối thủ
  ở ô kề; **aggressive_strategy** tiếp tục ưu tiên tiến về goal.
- Hàm **choose_action(state)** vẫn được giữ làm giao diện cho arena, nên không
  cần sửa code điều phối trận đấu khi thay đổi cách triển khai bên trong.
- Dữ liệu thiếu hoặc sai kiểu khiến policy mặc định trả về **wait**.

Đây là **composition** theo note Week 14: truyền hành vi vào object thay vì
hardcode một chiến thuật trong class. Không cần inheritance vì các strategy
không phải là những loại con của một class nền; các function đã đủ cho nhiệm vụ.

## 3. Hành trình W07–W15

| Week | Milestone | Điều bot học thêm |
|---|---|---|
| W07 | Function Bot | Quyết định xác định bằng function |
| W08 | State + Heuristic | State có cấu trúc và rule dễ giải thích |
| W09 | Midterm Bot V1 | Ghép các phần thành bot chạy local |
| W10 | Replay + Data | Lưu evidence bằng file, JSON và CSV |
| W11 | Robust Bot | Phân biệt lỗi phần mềm với thua chiến thuật |
| W12 | Tested Bot | Khóa hành vi bằng regression tests |
| W13 | Adapter Boundary | Tách bot core khỏi runtime adapter |
| W14 | Strategy Composition | Thay strategy mà không viết lại core |
| W15 | Capstone Tournament | Tích hợp, kiểm thử, đánh giá và demo |

## 4. Cài đặt

Yêu cầu Python 3.10+ và pytest. Từ thư mục gốc repository:

```bash
python -m pip install pytest
```

Phần chạy bot chỉ sử dụng Python standard library; không cần API key hoặc
network access.

## 5. Sử dụng

Chạy một match giữa student bot và baseline:

```bash
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a student --bot-b forward --replay
```

Chạy tournament với ba baseline:

```bash
python projects/vuacoc-bot-journey/local_arena/tournament_cli.py
```

Chạy ví dụ quyết định độc lập:

```bash
python projects/vuacoc-bot-journey/student_bot/bot.py
```

## 6. Chạy test

Chạy test của project từ thư mục gốc:

```bash
python -m pytest projects/vuacoc-bot-journey/tests -q
```

Chạy readiness check cho capstone:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py projects/vuacoc-bot-journey
```

Các test kiểm tra hướng đi tới goal, action hợp lệ, state lỗi, tính xác định
(determinism), và việc thay strategy thông qua composition.

## 7. Cấu trúc chính

- **student_bot/bot.py**: class Bot, các strategy và giao diện choose_action.
- **local_arena/**: match loop, contract, replay và CLI.
- **baselines/**: các bot đối chứng đơn giản.
- **tests/**: regression tests cho bot, arena, replay và tournament.
- **AI_USAGE.md**: công khai việc sử dụng AI hỗ trợ.

## 8. Giới hạn đã biết

- Đây là policy cơ bản, không phải chiến thuật tối ưu; bot có thể hòa.
- Tên aggressive_strategy chỉ mang nghĩa tiếp tục tiến về goal trong local
  arena. Arena không có action tấn công riêng.
- Defensive policy có thể chờ khi đối thủ ở gần, làm giảm tốc độ tiến tới goal.
- Tournament chỉ đo hành vi trong mô hình local; không đại diện hiệu năng thực tế.
- Contract production của VuaCóc chưa được xác minh; project không tuyên bố tích
  hợp production.

## 9. AI usage

Xem [AI_USAGE.md](AI_USAGE.md) để biết AI đã hỗ trợ những phần nào và cách các
đề xuất được kiểm chứng. Người học cần tự chạy test, đọc code và hiểu các quyết
định thiết kế trước khi nộp.
