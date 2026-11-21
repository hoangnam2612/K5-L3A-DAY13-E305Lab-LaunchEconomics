# Báo cáo cá nhân — Nguyễn Đức Trọng (2A202603644)

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Đức Trọng
- **Mã học viên:** 2A202603644
- **Email:** Bổ sung email sử dụng trong nhóm/LMS.
- **Vai trong nhóm:** Người gắn nhãn 1.

## 2. Phần việc phụ trách

Trong vai trò **Người gắn nhãn 1**, tôi phụ trách theo dõi yêu cầu hoàn thành của các checkpoint, tập trung vào kiểm soát chất lượng nội dung và tính nhất quán của hồ sơ nhóm. Phần việc chính gồm:

- Theo dõi các điều kiện **“Xong khi”** trong `CHECKPOINTS.md`, nhắc nhóm kiểm tra sản phẩm đầu ra trước khi chuyển checkpoint.
- Phụ trách phần gắn nhãn độc lập tại **CP3**, nghiên cứu định nghĩa năm nhóm lỗi, phân loại theo nguyên nhân gốc và phối hợp đối chiếu với Người gắn nhãn 2 sau khi hai bộ nhãn đã được hoàn thành độc lập.
- Rà soát bảng khắc phục lỗi để bảo đảm mỗi loại lỗi có cách phát hiện đo được, hành động khắc phục và một vai trò chịu trách nhiệm.
- Hỗ trợ rà soát **CP4 – Pilot plan** và **CP5 – Launch v0**, tập trung vào tính hợp lý của phương án thử nghiệm, điều kiện dừng, cách đo lường và mức độ nhất quán giữa số liệu với đề xuất cuối.

## 3. Đóng góp cụ thể

### CP1 – Mô hình chi phí mỗi việc thành công

- Theo dõi các điều kiện hoàn thành của nhiệm vụ A, đặc biệt là việc phân biệt chi phí của agent với chi phí nhân sự tham gia xem lại và làm lại.
- Rà soát cách trình bày các khoản chi phí và nhắc nhóm gắn nhãn `simulated` cho những kết quả được tính từ các trường dữ liệu giả lập.
- Kiểm tra tính nhất quán giữa chi phí mỗi việc thành công, chi phí của phạm vi pilot và phần phân bổ chi phí cố định; tránh sử dụng các chỉ số này thay thế cho nhau.

### CP2 – Bảng độ nhạy

- Theo dõi mức độ đầy đủ của các kịch bản phân tích độ nhạy và yêu cầu kết luận phải có số liệu đi kèm.
- Hỗ trợ diễn giải ý nghĩa kinh doanh của các yếu tố nhạy nhất: thời gian làm lại, thời gian xem lại và chi phí nhân công.
- Nhấn mạnh rằng tối ưu số lần retry hoặc chi phí token riêng lẻ chưa chắc làm giảm tổng chi phí vận hành của doanh nghiệp.

### CP3 – Bảng lỗi và cách khắc phục

- Nghiên cứu và sử dụng năm nhóm phân loại lỗi theo Google PAIR: **Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm**.
- Thực hiện phần việc của Người gắn nhãn 1 theo nguyên tắc phân loại dựa trên **nguyên nhân gốc**, không dựa trên bộ phận sẽ chịu trách nhiệm sửa lỗi.
- Phối hợp chuẩn bị quy trình đối chiếu hai bộ nhãn độc lập; các ca bất đồng cần có giải thích và quy tắc phân biệt thay vì chỉ thay nhãn để khớp nhau.
- Rà soát bảng khắc phục năm tình huống đại diện, tập trung vào tính đo được của cơ chế phát hiện, hành động xử lý và vai trò chịu trách nhiệm.
- Đề xuất làm rõ các kiểm soát quan trọng như đối soát trạng thái hoàn tiền với ledger, chống giao dịch trùng, nhận diện mã đơn từ sàn thương mại điện tử và kiểm tra phiên bản bảng giá.

> **Thông tin cần cập nhật trước khi nộp:** điền kết quả 20 nhãn độc lập của cá nhân, kết quả đối chiếu với Người gắn nhãn 2 và tỷ lệ đồng thuận thực tế vào `report/team/bang_loi.md`. Không ghi tỷ lệ đồng thuận hoặc xác nhận hoàn thành nếu hai bộ nhãn độc lập chưa được lưu lại.

### CP4 – Thiết kế pilot

- Rà soát logic lựa chọn đơn vị chia nhóm và lý do không chọn chia theo từng yêu cầu hoặc theo depot.
- Nắm và giải thích được phương án 20 nhân viên dùng AI và 20 nhân viên đối chứng; mức chênh lệch mục tiêu 6 điểm phần trăm, cỡ mẫu hiệu dụng 859 mỗi nhóm và Design Effect 6,96.
- Chỉ ra đánh đổi thống kê cần công khai: nếu hiệu quả thực tế chỉ là 5 điểm phần trăm, power của phương án được chọn còn khoảng 0,64, do đó cần người có thẩm quyền chấp nhận trước khi bắt đầu pilot.
- Rà soát năm nội dung về khả năng tách tác động: chạy đồng thời, phân nhóm ngẫu nhiên, nguy cơ ảnh hưởng chéo, chốt trước chỉ số và ngưỡng, số cụm mỗi nhóm.
- Kiểm tra các stop rules về an toàn, chi phí và mức độ sử dụng; lưu ý cần diễn đạt rõ ngưỡng, khoảng thời gian, người có quyền dừng và hành động khi không vi phạm.

### CP5 – Chỉ số, rủi ro và hồ sơ Launch v0

- Rà soát ba chỉ số được tính thử trên mẫu: tỷ lệ đóng trong 24 giờ và không mở lại trong 7 ngày **82,83% (994/1.200)**; tỷ lệ sửa hoặc bỏ gợi ý **27,12% (48/177)**; tỷ lệ mở lại trong 7 ngày **4,25% (51/1.200)**.
- Nhấn mạnh giới hạn diễn giải: 82,83% là kết quả quan sát trong đợt chạy thử, không đủ để kết luận trợ lý đã cải thiện 12,83 điểm phần trăm so với baseline 70% vì chưa có nhóm đối chứng đồng thời.
- Rà soát danh sách event và vai trò của `trace_id` trong việc nối các bước từ lúc tạo yêu cầu, chạy agent, nhân viên xem lại, ghi ledger đến khi đóng hoặc mở lại ticket.
- Đối chiếu các rủi ro kinh tế với bảng độ nhạy; kiểm tra hồ sơ Launch v0 có nêu cả số liệu thuận lợi lẫn bất lợi và không trình bày dữ liệu `simulated` như kết quả vận hành thực tế.
- Hỗ trợ chuẩn bị lập luận bảo vệ đề xuất **Go có điều kiện**, giới hạn phạm vi pilot ở `noi_dia` và `hang_nang`, đồng thời nêu rõ các điều kiện cần hoàn thành trước khi bắt đầu.

## 4. Bằng chứng

Các tài liệu và phần việc liên quan đến vai trò của tôi:

- `CHECKPOINTS.md`: checklist điều kiện hoàn thành CP1–CP5.
- `TEAM.md`: phân công vai trò Người gắn nhãn 1 và trách nhiệm theo dõi checkpoint.
- `report/team/bang_loi.md`: bộ nhãn độc lập, kết quả đối chiếu và bảng khắc phục CP3.
- `report/team/pilot_plan.yaml`: phương án phân nhóm, cỡ mẫu, đánh đổi thống kê và stop rules CP4.
- `report/team/chi_so.md`: KPI, event tracking và rủi ro kinh tế CP5.
- `report/team/ho_so_launch_v0.md`: phần tổng hợp bằng chứng và đề xuất Gate 2a.

**Bằng chứng cá nhân cần bổ sung khi chốt repo:** link commit/PR do cá nhân tạo (nếu có), kết quả bộ nhãn độc lập của Người gắn nhãn 1 và phần nội dung đã trực tiếp chỉnh sửa trong các file nhóm.

## 5. Công cụ AI đã dùng

- **ChatGPT:** sử dụng để giải thích yêu cầu CP3–CP5, hệ thống hóa tiêu chí phân loại lỗi, làm rõ khái niệm thiết kế pilot/cỡ mẫu/nhóm đối chứng, chuẩn bị câu trả lời debate và rà soát tính nhất quán của hồ sơ.
- **Cách tự kiểm tra:** đối chiếu nội dung với `CHECKPOINTS.md`, `RULES.md`, `RUBRIC.md` và các file báo cáo hiện có trong repo; chỉ sử dụng số liệu đã xuất hiện trong kết quả tính toán hoặc hồ sơ nhóm; không sử dụng câu trả lời AI thay cho hai bộ nhãn độc lập, kết quả chạy code hay quyết định của hội đồng.

## 6. Tự đánh giá

Tôi đã tập trung vào vai trò kiểm soát chất lượng: theo dõi điều kiện hoàn thành, xem xét nguyên nhân gốc của lỗi và kiểm tra xem các quyết định về pilot có được hỗ trợ bởi dữ liệu hay không. Qua bài lab, tôi hiểu rõ hơn rằng đánh giá một AI Agent không thể chỉ dựa trên việc agent trả lời đúng hoặc chi phí token thấp; cần tính cả thời gian con người can thiệp, mức độ nhân viên sử dụng, rủi ro nghiệp vụ và khả năng đo lường tác động bằng nhóm đối chứng.

Điểm cần cải thiện của tôi là tăng mức độ chủ động lưu bằng chứng công việc theo từng checkpoint, đặc biệt là kết quả gắn nhãn độc lập, các quyết định khi xử lý ca bất đồng và commit tương ứng. Ở các bài tiếp theo, tôi sẽ chuẩn hóa checklist và ghi nhận kết quả ngay khi hoàn thành từng đầu việc để việc kiểm tra chéo và đánh giá đóng góp cá nhân rõ ràng hơn.
