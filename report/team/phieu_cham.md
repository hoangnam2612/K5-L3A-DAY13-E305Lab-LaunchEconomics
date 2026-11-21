# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ...
- Nhóm được chấm: ...

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 9.5 | Đề xuất Go có điều kiện phù hợp với chi phí `noi_dia` 0,22× và `hang_nang` 0,69× so với 12.000 đ; loại `quoc_te` vì 1,88× và thành công 27,3%. Nhóm nêu bất lợi: xem lại 100% có thể lên 1,03× và power chỉ 0,64 nếu tác động thật là 5 điểm. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các chi phí dùng phút `_simulated` được ghi nhãn simulated; phạm vi chỉ gồm `noi_dia` + `hang_nang` dựa trên 2.696 đ và 8.221 đ/việc. `quoc_te` (22.515 đ) và `doi_tac` có điều khoản riêng đều bị loại khỏi pilot. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 9 | Chia ngẫu nhiên 20 + 20 nhân viên, có đối chứng song song và 3 luật dừng có ngưỡng/thời hạn/owner. Pilot đủ 859 yêu cầu mỗi nhánh để phát hiện chênh 6 điểm, nhưng chưa đủ 1.251 yêu cầu cho mục tiêu 5 điểm; đây là đánh đổi đã nêu rõ. |
| **Tổng** | | | | **28.5 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Cho phép pilot thu hẹp với `noi_dia` + `hang_nang` sau khi sửa khóa chống trùng và đối soát sổ cái. Trước khi bắt đầu, Giám đốc vận hành phải ký chấp nhận MDE 6 điểm; PM phải bật đủ event có `trace_id` và thay phút simulated bằng phút đo thật sau tuần 1.

**Một câu hỏi cho đội trình:** Nếu tuần đầu phải xem lại 100% gợi ý, chi phí có thể lên 0,98×–1,03× baseline; tiêu chí nào cho phép nhóm giảm xem lại ở bước rollout tiếp theo mà vẫn giữ an toàn?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
