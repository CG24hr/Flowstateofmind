# column แรก คืออัตราส่วน post bronchodilator FEV1/FVC ของผู้ป่วย COPD ที่มาทดสอบ
# column สอง คืออัตราส่วน FEV1 ของผู้ป่วยเทียบกับค่ามาตรฐาน หลังได้รับ bronchodilator
# กำหนดให้ FEV1/FVC < 70% = COPD 
# แสดงผล ความรุนแรงของปอดอุดกั้นเรื้อรัง 
    # stage I >= 80
    # 50 <= stage II < 80
    # 30 <= stage III < 50
    # stage IV < 30
# ทำกราฟแสดงความสัมพันธ์ระหว่าง FEV1/FVC กับ staging ของ COPD 

data = [[60,65],
        [55,60],
        [40,30],
        [50,45],
        [45,55]]

import numpy as np
import matplotlib.pyplot as plt
data_np = np.array(data)

FEV1perFVC = data_np[:, 0]
FEV1ratio = data_np[:, 1]
severity = []
for i in FEV1ratio :
    if i >= 80 :
        severity.append(1)
    elif 50 <= i < 80 :
        severity.append(2)
    elif 30 <= i < 50 :
        severity.append(3)
    else :
        severity.append(4)
severity_np = np.array(severity)

print('Post Bronchodilator FEV1/FVC of COPD patients are ', FEV1perFVC)
print('Post Bronchodilator FEV1ratio compared to standard FEV1 of COPD patients are ', FEV1ratio)
print('Severity of COPD in these patients are ', severity)
III = severity_np[severity_np > 2]
print('The number of patients who have third stage of COPD or more is ', len(III) )

plt.xlabel('FEV1perFVC')
plt.ylabel('severity')
plt.title('COPD staging')
plt.bar(FEV1perFVC, severity)
plt.show()




