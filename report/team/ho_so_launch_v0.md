# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ... · Lớp: ...

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool (274,7 đ); trong phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 4.599 đ | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại (+51,8%) · tỉ lệ xem lại (+40,7%) · lương nhân viên (+23,1%) [simulated]; giá token chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; `noi_dia` 0,22×, `hang_nang` 0,69×, `quoc_te` 1,88×, `doi_tac` 0,85×; xem lại 100%: 0,98× (1,03× với làm lại 15,3 phút) | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); đợt chạy thử không có đối chứng | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đã có nhãn thống nhất 20 ca và khắc phục 5 ca đủ năm loại; hai bộ nhãn độc lập và tỉ lệ đồng thuận (cần ≥ 16/20) chưa có | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, 859/nhóm (mức chênh 6 điểm, DE 6,96); cỡ mẫu cho 5 điểm là 1.251/nhóm, không đạt; 3 luật dừng | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ · xem lại 100% kéo dài: 0,98×–1,03× · khối lượng giảm một nửa: +2.370 đ/việc cố định [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- **Go có điều kiện** cho pilot chỉ gồm `noi_dia` + `hang_nang`; loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×). Con số bất lợi: pilot chỉ thấy được mức chênh 6 điểm, nếu tác động thật là 5 điểm thì power còn khoảng 0,64; chi phí 0,49× dựa trên phút giả lập.
  1. Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước khi bắt đầu. Người phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-12-22.
  2. Ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm). Người phụ trách: Giám đốc vận hành. Kiểm tra: 2026-12-22.
  3. Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1. Người phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2027-01-05.
  4. Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% không tiết kiệm (0,98×–1,03×). Người phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2027-01-05.
  5. Hoàn tất hai bộ nhãn độc lập cho bảng lỗi, đồng thuận ≥ 80%. Người phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-12-22.
