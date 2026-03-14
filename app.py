import streamlit as st
import pandas as pd
import pickle as pkl
import re
from underthesea import word_tokenize
from underthesea import text_normalize
#Tải các thành phần cần thiết
model = pkl.load(open("academic_classfier_xgbmodel.pkl","rb"))
preprocessor = pkl.load(open("preprocessor.pkl","rb"))
te_stats = pkl.load(open("target_encoding_maps.pkl", "rb"))
# Phương thức để xử lý dữ liệu văn bản
# Loại bỏ ký tự thừa bị lặp ở cuối. Ví dụ: "vuiii" -> "vui", "trạngg" -> "trạng"
def remove_vietnamese_trailing_repeats(text):
    if not isinstance(text, str):
        return text
    
    # Biểu thức chính quy: 
    # (\w) : Khớp với một ký tự chữ bất kỳ và nhóm nó lại (nhóm 1)
    # \1+  : Khớp với ký tự trong nhóm 1 lặp lại 1 hoặc nhiều lần
    # $    : Chỉ khớp nếu việc lặp lại này xảy ra ở CUỐI từ
    
    processed_text = re.sub(r'(\w)\1+\b', r'\1', text)
    
    return processed_text
# Tạo từ điển teencode đã tìm thấy trong bộ dữ liệu
teencode_dict = {
    "lun": "luôn", "khong": "không", "hoc": "học", "dc": "được", 
    "duoc": "được", "bít": "biết", "mk": "mình", "nhung": "nhưng", 
    "nhg": "nhưng", "viec": "việc", "hông": "không", "vs": "với", 
    "ko": "không", "bit": "biết", "k": "không", "e": "em", 
    "qa": "quá", "j": "gì"
}

def fix_teencode(text):
    if not isinstance(text, str):
        return text
    
    # Tách từ để xử lý chính xác (tránh sửa nhầm từ nằm trong từ khác)
    words = text.split()
    fixed_words = [teencode_dict.get(w.lower(), w) for w in words]
    
    return " ".join(fixed_words)
#Xử lý thuộc tính văn bản
def clean_text(text):
    if not isinstance(text, str):
        return ""

    #Xử lý dấu câu
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    #Chuyển về chữ thường
    text = text.lower()

    #Loai bỏ ký tự lặp ở cuối câu
    text = remove_vietnamese_trailing_repeats(text)

    #Chỉnh sửa teencode
    text = fix_teencode(text)

    text = word_tokenize(text, format="text")
    return text

#Tạo giao diện và đầu vào
st.title("Dự đoán tình trạng học tập sinh viên")
with st.form("student_data"):
    gender = st.selectbox("Giới tính", ["Nam", "Nữ"])
    admission = st.selectbox("Phương thức tuyển sinh", ["Thi THPT", "Xét học bạ", "ĐGNL", "Tuyển thẳng"])
    english = st.selectbox("Trình độ Tiếng Anh", ["A1", "A2", "B1", "B2", "IELTS 6.0+"])
    club = st.selectbox("Có tham gia câu lạc bộ không", ["Yes", "No"])
    tuition = st.number_input("Nợ học phí", min_value=0)
    count_f = st.number_input("Số điểm F", min_value=0)
    notes = st.text_area("Nhận xét của cố vấn học tập")
    essay = st.text_area("Bài luận cá nhân")
    att1 = st.number_input('Chuyên cần môn 1', min_value=-1, max_value=16)
    att2 = st.number_input('Chuyên cần môn 2', min_value=-1, max_value=16)
    att3 = st.number_input('Chuyên cần môn 3', min_value=-1, max_value=16)
    att4 = st.number_input('Chuyên cần môn 4', min_value=-1, max_value=16)
    att5 = st.number_input('Chuyên cần môn 5', min_value=-1, max_value=16)
    att6 = st.number_input('Chuyên cần môn 6', min_value=-1, max_value=16)
    att7 = st.number_input('Chuyên cần môn 7', min_value=-1, max_value=16)
    att8 = st.number_input('Chuyên cần môn 8', min_value=-1, max_value=16)
    att9 = st.number_input('Chuyên cần môn 9', min_value=-1, max_value=16)
    att10 = st.number_input('Chuyên cần môn 10', min_value=-1, max_value=16)
    att11 = st.number_input('Chuyên cần môn 11', min_value=-1, max_value=16)
    att12 = st.number_input('Chuyên cần môn 12', min_value=-1, max_value=16)
    att13 = st.number_input('Chuyên cần môn 13', min_value=-1, max_value=16)
    att14 = st.number_input('Chuyên cần môn 14', min_value=-1, max_value=16)
    att15 = st.number_input('Chuyên cần môn 15', min_value=-1, max_value=16)
    att16 = st.number_input('Chuyên cần môn 16', min_value=-1, max_value=16)
    att17 = st.number_input('Chuyên cần môn 17', min_value=-1, max_value=16)
    att18 = st.number_input('Chuyên cần môn 18', min_value=-1, max_value=16)
    att19 = st.number_input('Chuyên cần môn 19', min_value=-1, max_value=16)
    att20 = st.number_input('Chuyên cần môn 20', min_value=-1, max_value=16)
    att21 = st.number_input('Chuyên cần môn 21', min_value=-1, max_value=16)
    att22 = st.number_input('Chuyên cần môn 22', min_value=-1, max_value=16)
    att23 = st.number_input('Chuyên cần môn 23', min_value=-1, max_value=16)
    att24 = st.number_input('Chuyên cần môn 24', min_value=-1, max_value=16)
    att25 = st.number_input('Chuyên cần môn 25', min_value=-1, max_value=16)
    att26 = st.number_input('Chuyên cần môn 26', min_value=-1, max_value=16)
    att27 = st.number_input('Chuyên cần môn 27', min_value=-1, max_value=16)
    att28 = st.number_input('Chuyên cần môn 28', min_value=-1, max_value=16)
    att29 = st.number_input('Chuyên cần môn 29', min_value=-1, max_value=16)
    att30 = st.number_input('Chuyên cần môn 30', min_value=-1, max_value=16)
    att31 = st.number_input('Chuyên cần môn 31', min_value=-1, max_value=16)
    att32 = st.number_input('Chuyên cần môn 32', min_value=-1, max_value=16)
    att33 = st.number_input('Chuyên cần môn 33', min_value=-1, max_value=16)
    att34 = st.number_input('Chuyên cần môn 34', min_value=-1, max_value=16)
    att35 = st.number_input('Chuyên cần môn 35', min_value=-1, max_value=16)
    att36 = st.number_input('Chuyên cần môn 36', min_value=-1, max_value=16)
    att37 = st.number_input('Chuyên cần môn 37', min_value=-1, max_value=16)
    att38 = st.number_input('Chuyên cần môn 38', min_value=-1, max_value=16)
    att39 = st.number_input('Chuyên cần môn 39', min_value=-1, max_value=16)
    att40 = st.number_input('Chuyên cần môn 40', min_value=-1, max_value=16)
    submit = st.form_submit_button("Dự đoán")
if submit:
    # Tạo DataFrame từ input
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Admission_Mode": admission, 
        "English_Level": english,
        "Club_Member": club,
        "Tuition_Debt": float(tuition), 
        "Count_F": count_f,
        "Advisor_Notes": clean_text(notes),
        "Personal_Essay": clean_text(essay),
        "Att_Subject_01": att1,
        "Att_Subject_02": att2,
        "Att_Subject_03": att3,
        "Att_Subject_04": att4,
        "Att_Subject_05": att5,
        "Att_Subject_06": att6,
        "Att_Subject_07": att7,
        "Att_Subject_08": att8,
        "Att_Subject_09": att9,
        "Att_Subject_10": att10,
        "Att_Subject_11": att11,
        "Att_Subject_12": att12,
        "Att_Subject_13": att13,
        "Att_Subject_14": att14,
        "Att_Subject_15": att15,
        "Att_Subject_16": att16,
        "Att_Subject_17": att17,
        "Att_Subject_18": att18,
        "Att_Subject_19": att19,
        "Att_Subject_20": att20,
        "Att_Subject_21": att21,
        "Att_Subject_22": att22,
        "Att_Subject_23": att23,
        "Att_Subject_24": att24,
        "Att_Subject_25": att25,
        "Att_Subject_26": att26,
        "Att_Subject_27": att27,
        "Att_Subject_28": att28,
        "Att_Subject_29": att29,
        "Att_Subject_30": att30,
        "Att_Subject_31": att31,
        "Att_Subject_32": att32,
        "Att_Subject_33": att33,
        "Att_Subject_34": att34,
        "Att_Subject_35": att35,
        "Att_Subject_36": att36,
        "Att_Subject_37": att37,
        "Att_Subject_38": att38,
        "Att_Subject_39": att39,
        "Att_Subject_40": att40
    }])
    for col in ["Admission_Mode", "English_Level"]:
        target_col_name = f"{col}_te"
        mapping_info = te_stats[col][1] 
        input_df[target_col_name] = input_df[col].map(mapping_info["map"]).fillna(mapping_info["global_mean"])
    input_df_final = input_df.drop(columns=["Admission_Mode", "English_Level"])
    
    input_scaled = preprocessor.transform(input_df_final)
    prediction = model.predict(input_scaled)
    result_map = {0: "Bình thường", 1: "Cảnh báo", 2: "Buộc thôi học"}
    res_text = result_map.get(prediction[0], prediction[0])
    st.success(f"### Dự đoán Tình trạng: **{res_text}**")