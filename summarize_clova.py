# -*- coding: utf-8 -*-
import my_account
import requests
import json
client_id = my_account.CLIENT_ID
client_secret = my_account.CLIENT_SECRET
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}
language = "ko" # Language of document (ko, ja )
model = "news" # Model used for summaries (general, news)
tone = "3" # Converts the tone of the summarized result. (0, 1, 2, 3)
summaryCount = "3" # This is the number of sentences for the summarized document.
url= "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"
title= "첨단재생의료실시기관 9개소 추가 지정, 총 85개소로 확대"
content = "보건복지부(장관 조규홍)는 2023년도 4분기 첨단재생의료실시기관(이하 재생의료기관) 지정심사 결과, 상급종합병원 3개, 종합병원 3개, 병원 3개 등 신규 9개소를 추가 지정하여, 2023년 총 29개소가 신규 지정되었다고 밝혔다. 「첨단재생바이오법」제10조에 따라, 첨단재생의료 임상연구(세포 유전자 조직 융복합치료)를 하려 의료기관은 보건복지부장관으로부터 첨단재생의료실시기관으로 지정을 받아야 함. 이로써 2023년 12월 현재 첨단재생의료를 실시할 수 있는 재생의료기관은 누적 총 85개소로 확대되어, 보다 많은 임상 현장에서 첨단재생의료 임상연구 준비가 가능할 것으로 기대된다. 상급종합병원 42개소, 종합병원 33개소, 병원 7개소, 의원 3개소, 첨단재생의료실시기관으로 지정받기 위해서는 「첨단재생의료 안전 및 지원에관한 규칙」제3조 및 별표1 등에 따른 시설·장비·인력, 표준작업지침서를 갖추어야 하고, 필수 인력(연구책임자, 연구담당자, 인체세포등 관리자, 정보관리자)은 보건복지부장관이 정하는 교육을 이수해야 한다. 보건복지부는 서류검증 및 현장실사 등을 거쳐 지정 여부를 결정하게 된다. 첨단재생의료실시기관 2023년도 공모‧접수 기간은 12월 22일(금)까지로 마감되며, 2024년도 1분기에 심사를 진행할 예정이다. 한편 내년도 공모시기는 1분기 중 시작하여 상시 공모할 계획이다. 지정 신청을 위한 제출서류 및 제출방법 등 자세한 사항은 재생의료진흥재단 사전 상담 절차*를 통해 신청에 필요한 상담을 받을 수 있으며, 첨단재생의료 누리집을 통해서도 확인할 수 있다. 문의처(재생의료진흥재단 실시기관지정팀) 보건복지부 김영학 재생의료정책과장은 '첨단재생의료실시기관을 지속적으로 확대하고 다양한 임상연구를 촉진하여 더 많은 환자분들께 치료 기회를 드릴 수 있도록, 의료질 평가지표 반영('23년~), 고위험 임상연구 신속‧병합심사 도입('23년~), 임상연구비용 지원(21년~) 등 정책적 노력을 기울이고 있다'라며, '전국의 역량 있는 의기관들의 많은 관심과 참여를 부탁드린다' 라고 전했다."
data = {
    "document": {
    "title": title,
    "content" : content
    },
    "option": {
    "language": language,
    "model": model,
    "tone": tone,
    "summaryCount" : summaryCount
    }
}
print(json.dumps(data, indent=4, sort_keys=True))
response = requests.post(url, data=json.dumps(data), headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)
