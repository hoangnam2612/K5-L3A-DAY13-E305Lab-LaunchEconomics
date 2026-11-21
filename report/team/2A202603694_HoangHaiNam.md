# Báo cáo cá nhân — HoangHaiNam-2A202603694

## 1. Thông tin thành viên

- Họ tên: Hoàng Hải Nam
- MSSV: 2A202603694
- Email: 26ai.namhh2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

Viết và chạy `src/lab13.py`, và điền các bảng số liệu của nhiệm vụ A, B và D1 vào `report/team/bang_chi_phi.md` và `report/team/pilot_plan.yaml`. Cùng nhóm hoàn thiện nhiệm vụ E (`chi_so.md`, `ho_so_launch_v0.md`) và `group_report.md` từ các số đã tính. Nhiệm vụ C (gắn nhãn 20 ca lỗi) do hai bạn gắn nhãn của nhóm làm độc lập; tôi không tham gia gắn nhãn.

## 3. Đóng góp cụ thể

- **A1:** viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** viết `mo_hinh`: cộng token và tool của mọi lần chạy, cộng phút xem lại và làm lại [simulated], chia cho số việc thành công. Kết quả: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool (274,7 đ).
- **A3, A4:** tách theo bốn loại yêu cầu (noi_dia 2.696 đ, hang_nang 8.221 đ, doi_tac 10.215 đ, quoc_te 22.515 đ) và tính tỉ lệ ok theo lần thử; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang (4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× ở một nửa khối lượng) [simulated].
- **B:** chín kịch bản độ nhạy (B1), một cặp (B2), giới hạn 1–3 lần chạy với chi phí cả hệ thống (B3), xem lại 100% (B4). Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- **D1:** cỡ mẫu theo ba cách chia (1.251 mỗi nhóm khi chia theo yêu cầu; 3.103 mỗi nhóm và 42 người mỗi nhóm khi chia theo nhân viên, không đủ người; tối đa 1.000 với 20 nhân viên mỗi nhóm; tối đa 300 với 6 depot; 299 yêu cầu mỗi người ở mức chênh 6 điểm). Chọn chia theo nhân viên 20 + 20 và ghi đánh đổi vào `pilot_plan.yaml`.
- **E:** tính thử ba chỉ số (82,83% · 27,12% · 4,25%), liệt kê chín event có `trace_id`, và điền hồ sơ launch v0 với đề xuất Go có điều kiện.

## 4. Bằng chứng

- Commit trên nhánh `main`: `1e49339` (done A1, A2), `07481cc` (done nhiem vu A), `c59ee3e` (done nhiem vu B), `0da7550` (done nhiem vu C,D,E).
- File: `src/lab13.py` (chạy `python lab13.py` trong `src/` in ba phép thử ĐẠT và các bảng A2, A3, A4, B1–B4, D1); `report/team/bang_chi_phi.md`; `report/team/pilot_plan.yaml`; `report/team/chi_so.md`; `report/team/ho_so_launch_v0.md`.
- Con số tự đối chiếu với đề: tổng chi phí 4.373.585 đ, 978 việc thành công, 4.472 đ mỗi việc thành công; các dòng B1 khớp đến từng đồng, và mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của kịch bản "gấp đôi" tương ứng.

## 5. Công cụ AI đã dùng

Claude Code (Anthropic). Dùng để đọc đề và tài liệu hướng dẫn, viết code trong `lab13.py`, điền các bảng báo cáo và giải thích lại cách tính. Cách tự kiểm tra:
- chạy lại `python lab13.py` và đối chiếu từng số với bảng đáp án trong tài liệu hướng dẫn;
- đếm lại bằng pandas những chỗ đề viết không khớp (ví dụ 222 = 148 chuyển nhân viên + 74 làm lại; phút làm lại trung bình 15,3 trên 74 ca);
- kiểm tra `git diff` để chắc các dòng `TODO` và chú thích gốc của đề không bị xoá;
- kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?` ngoài chú thích.

Nhóm cần xem lại nội dung lấy từ bài mẫu của tài liệu hướng dẫn (người phụ trách, ngày kiểm tra, ngày quyết định trong hồ sơ và pilot plan).

## 6. Tự đánh giá

Điểm làm tốt: mọi số chính khớp đáp án của đề, mọi số tính từ cột `_simulated` đều ghi nhãn simulated, và code chạy được từ đầu đến cuối. Điểm cần cải thiện: bảng khắc phục lỗi và các ngưỡng, người phụ trách trong pilot plan cần được cả nhóm thảo luận lại theo thực tế, thay vì giữ nguyên bài mẫu; phút xem lại và làm lại vẫn là số giả lập nên kết luận về chi phí phải được thay bằng số đo thật sau tuần 1 của pilot.
