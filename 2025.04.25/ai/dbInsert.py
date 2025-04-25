from pymongo import MongoClient

sample_clauses = [
    # 퇴직금 관련
    { "clause": "퇴직금은 퇴직일로부터 14일 이내에 지급해야 한다.", "category": "퇴직금" },
    { "clause": "근로자가 퇴직할 경우, 회사는 2주 이내에 퇴직금을 정산하여 지급한다.", "category": "퇴직금" },
    { "clause": "퇴직 후 퇴직금은 법정 기한인 14일 내로 송금되어야 한다.", "category": "퇴직금" },
    { "clause": "퇴사 후 퇴직금은 특별한 사유가 없는 한 즉시 지급되어야 한다.", "category": "퇴직금" },
    { "clause": "퇴직금은 근속 연수에 따라 계산되며, 평균임금을 기준으로 산정된다.", "category": "퇴직금" },
    { "clause": "퇴직금 산정 시 마지막 3개월 평균임금을 기준으로 한다.", "category": "퇴직금" },
    { "clause": "퇴직 시 잔여 연차 수당은 퇴직금과 함께 지급된다.", "category": "퇴직금" },
    { "clause": "정규직과 계약직 모두에게 퇴직금은 동일 기준으로 적용된다.", "category": "퇴직금" },
    { "clause": "퇴직금은 세법에 따라 과세 처리된다.", "category": "퇴직금" },
    { "clause": "퇴직 후 퇴직금 미지급 시 법적 조치를 취할 수 있다.", "category": "퇴직금" },

    # 연차휴가 관련
    { "clause": "연차 유급휴가는 1년 이상 근속 시 연 15일이 부여된다.", "category": "휴가" },
    { "clause": "신입사원은 1개월 만근 시 월 1일의 유급휴가를 받을 수 있다.", "category": "휴가" },
    { "clause": "연차는 사용자의 신청에 따라 자유롭게 사용 가능하다.", "category": "휴가" },
    { "clause": "미사용 연차는 다음 해로 이월되지 않는다.", "category": "휴가" },
    { "clause": "연차는 회사 업무에 지장이 없는 범위에서 사용해야 한다.", "category": "휴가" },
    { "clause": "연차 사용은 최소 3일 전에 신청해야 한다.", "category": "휴가" },
    { "clause": "연차는 법정 기준에 따라 발생하며, 근속기간에 비례하여 증가한다.", "category": "휴가" },
    { "clause": "사용하지 않은 연차는 연말 정산 시 수당으로 대체 가능하다.", "category": "휴가" },
    { "clause": "휴가는 팀장 승인 후 사용 가능하다.", "category": "휴가" },
    { "clause": "연차는 최대 1년간 이월이 가능하나 이후 소멸된다.", "category": "휴가" },

    # 근로시간 관련
    { "clause": "기본 근로시간은 주 5일, 하루 8시간이다.", "category": "근로시간" },
    { "clause": "주간 총 근무 시간은 40시간을 초과할 수 없다.", "category": "근로시간" },
    { "clause": "연장근무는 사전 승인 하에 1일 2시간, 주 12시간까지 가능하다.", "category": "근로시간" },
    { "clause": "법정 공휴일은 유급휴일로 간주한다.", "category": "근로시간" },
    { "clause": "점심시간은 근로시간에 포함되지 않는다.", "category": "근로시간" },
    { "clause": "시차 출퇴근 제도는 부서장 승인 후 이용 가능하다.", "category": "근로시간" },
    { "clause": "탄력적 근로시간제는 일정 기준에 따라 운영된다.", "category": "근로시간" },
    { "clause": "시간 외 근로는 초과수당으로 보상받는다.", "category": "근로시간" },
    { "clause": "법정 근로시간을 초과할 경우 추가 휴게시간이 부여된다.", "category": "근로시간" },
    { "clause": "공휴일 근무 시 대체휴일 또는 수당이 지급된다.", "category": "근로시간" },

    # 급여 관련
    { "clause": "급여는 매월 말일에 지정된 계좌로 이체된다.", "category": "급여" },
    { "clause": "임금 지급일이 공휴일인 경우, 그 전일에 지급한다.", "category": "급여" },
    { "clause": "기본급 외의 수당은 급여일에 함께 지급된다.", "category": "급여" },
    { "clause": "급여 명세서는 지급일 당일 전자문서로 제공된다.", "category": "급여" },
    { "clause": "야근수당은 실제 근무 시간에 따라 정산된다.", "category": "급여" },
    { "clause": "급여는 실수령액 기준으로 지급된다.", "category": "급여" },
    { "clause": "성과급은 연말 인사 평가에 따라 결정된다.", "category": "급여" },
    { "clause": "급여 지급일은 별도 공지 없이 변경되지 않는다.", "category": "급여" },
    { "clause": "지급된 급여에 대한 이의는 지급 후 7일 이내에 제기할 수 있다.", "category": "급여" },
    { "clause": "지각 및 결근은 급여에서 차감될 수 있다.", "category": "급여" },

    # 복지 관련
    { "clause": "정직원에게는 연 1회 종합건강검진이 제공된다.", "category": "복지" },
    { "clause": "사내식당은 전 직원에게 할인된 금액으로 제공된다.", "category": "복지" },
    { "clause": "경조사 발생 시 유급휴가와 경조금이 지급된다.", "category": "복지" },
    { "clause": "재직 2년 이상 직원에게는 명절 상여금이 지급된다.", "category": "복지" },
    { "clause": "자녀 학자금 지원은 일정 기준 충족 시 제공된다.", "category": "복지" },
    { "clause": "사내 도서관 및 휴게 공간은 자유롭게 이용 가능하다.", "category": "복지" },
    { "clause": "매년 여름, 전직원 대상 하계 휴가비가 지급된다.", "category": "복지" },
    { "clause": "직원 생일에는 축하 기프트가 제공된다.", "category": "복지" },
    { "clause": "임직원 할인몰을 통해 제품 구매 시 혜택이 주어진다.", "category": "복지" },
    { "clause": "복지포인트는 매년 초 일괄 지급된다.", "category": "복지" },
]

client = MongoClient("mongodb://localhost:27017/")
db = client["contract_db"]
collection = db["clauses"]

# 기존 데이터 삭제 후 삽입
collection.delete_many({})
collection.insert_many(sample_clauses)

print("계약 조항 데이터 삽입 완료!")