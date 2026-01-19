import pandas as pd
import numpy as np
dict_data = {"a": 1, "b": 2, "c": 3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)

list_data=["2026-1-19", 3.14, "abc", 100, True]
series_data = pd.Series(list_data)
print(type(series_data))
print(series_data)

dict_data = {"c0":[1,2,3], "c1":[4,5,6], "c2":[7,8,9], "c3":[10,11,12], "c4":[13,14,15]}
df=pd.DataFrame(dict_data)
print(type(df))
print(df)

#pandas 데이터내용 확인
#.columns : 컬럼이름확인
#.head() : 상위5개행확인 (괄호안에 숫자넣으면 그 숫자만큼 확인가능)
#.tail() : 하위5개행확인 (괄호안에 숫자넣으면 그 숫자만큼 확인가능)
#.shape : (행개수, 열개수) 형태로 출력
#.info() : 데이터프레임 요약정보 출력
#행과열의 크기
#컬럼명
#컬럼별 결측치
#컬럼별 데이터타입
#.type() : 데이터 타입 확인

#파일 불러오기
#형식     읽기       쓰기
#csv   read_csv   to_csv
#excel read_excel to_excel
#json  read_json  to_json
#html  read_html  to_html

# ./ 내가 있는 기준으로 하위폴더 이동 ./data/titanic.csv
# ../ 상위폴더 이동 ../data/titanic.csv

titanic=pd.read_csv("Titanic-Dataset.csv")
print(titanic.columns)
print(titanic.head())
print(titanic.tail(10))
print(titanic.shape)
print(titanic.info())
print(type(titanic))

#pandas에서 특정 열을 선택
#열 1개 선택 => series 객체 반환
#데이터 프레임의 열 데이터 1개만 선택할 때 2가지 방법
#1. 대괄호[] 안에 열이름 문자열 넣기
#2. 점. 표기법 (열이름이 공백이나 특수문자가 없을 때만 가능)
#열 n개 선택 => 데이터프레임 객체 반환
#데이터 프레임의 열 데이터 n개 선택할 때는 1방식
#이중대괄호[[]] 열 이름을 따옴표로 함께 입력
#만약에 열 1개를 데이터프레임객체로 추출하려면 [[]] 사용가능

names=titanic["Name"]
print(names.head())
names=titanic.Name
print(names.head())
print(type(names))
print(names.shape)
double_columns=titanic[["Sex", "Age"]]
print(double_columns.head())
print(type(double_columns))
print(double_columns.shape)

#pandas 데이터 필터링
#1. boolean 인덱싱 True값 행만 추출
#2. .isin() 각각의 요소가 데이터프레임 또는 시리즈에 존재하는지 확인한 후 True/False 반환
#3. .isna() 결측 값은 True, 결측 값이 아니면 False 반환
#4. .notna() 결측 값이 아니면 True, 결측 값이면 False 반환

print(double_columns["Age"] >=35)
above35=double_columns[double_columns["Age"] >=35]
print(above35.head()) #True

#성별 남자만 추출
male=double_columns[double_columns["Sex"]=="male"]
print(male.head())

print(titanic.head())
class_1=titanic[titanic["Pclass"].isin([1])]
print(class_1.head())

print(double_columns.head())
age2040=double_columns[double_columns["Age"].isin(np.arange(20,41))]
print(age2040.head())

print(double_columns.head(7))
class_2=double_columns[double_columns["Age"].isna()]
print(class_2.head(7)) #비어있는 cell true 반환

class_3=double_columns[double_columns["Age"].notna()]
print(class_3.head(7)) #비어있는 cell false 반환

#결측 값을 제거한 누락되지 않은 값을 확인
#행제거
print(double_columns.head(10))
age5=double_columns[double_columns["Age"].notna()]
print(age5.head(10))

#.dropna(axis=0)==.dropna() 결측값 들어있는 행제거
#.dropna(axis=1) 결측값 들어있는 열제거

print(titanic.head())
print(titanic.dropna())

print(titanic.dropna(axis=1).head())

#pandas 이름과 인덱스로 특정 행과 열 선택
#.loc[]: 행 이름과 열 이름 사용 -> dataframe객체.loc[행이름, 열이름]
#.iloc[]: 행 번호와 열 번호 사용 -> dataframe객체.iloc[행번호, 열번호]

name35=titanic.loc[titanic["Age"]==35, ["Name", "Age"]]
print(name35.head())

name35.iloc[[1,2,3],0]="No name"
print(name35.head())

#판다스 데이터 통계
#.mean() 평균
#.median() 중앙값
#.describe() 요약통계량(평균, 중앙값, 최소값, 최대값, 사분위수)
#.agg() 여러 통계량 한번에 계산
#모든 열에 여러 함수를 매핑: group.객체.agg([함수1, 함수2, ...])
#각 열마다 다른 함수를 매핑: group.객체.agg(열이름1=함수1, 열이름2=함수2, ...)
#.groupby() 그룹별로 나누기
#value_counts() 고유값과 빈도수 계산

print("----평균나이----")
print(titanic["Age"].mean())

print("----중앙값 나이----")
print(titanic["Age"].median())

print("----다양한 통계량 요약----")
print(titanic.describe())

print("----모든 열에 동일한 함수 적용----")
print(titanic[["Age", "Fare"]].agg(["mean", "std"]))

print("----열별 사용자 집계----")
agg_dict={"Age":["mean","min","max"], "Fare":["std","median"]}
print(titanic.agg(agg_dict))

print("----성별 기준으로 평균 나이 및 요금----")
titanic.groupby("Sex").agg({"Age":"mean", "Fare":"mean"})

print("----객실 등급 별 인원수----")
print(titanic["Pclass"].value_counts())

print("----성별 인원수----")
print(titanic["Sex"].value_counts())

print("----새로운 열 country 생성 USA----")
titanic["country"]="USA"
print(titanic.head())

print("----기존 열 계산해서 새로운 열 추가----")
titanic["Newage"]=titanic["Age"]+10
print(titanic)

#20세 미만이면 child, 아니면 adult
print("----20세 미만이면 child, 아니면 adult----")
titanic["AgeGroup"]="Adult"
titanic.loc[titanic["Age"]<20, "AgeGroup"]="Child"
print(titanic)

#데이터 프레임의 가장 마지막 인덱스 확보 후 행 추가
new_index=len(titanic)
print(new_index)
print(titanic.head())
titanic.loc[new_index]=[992,1,1,"shin","female",53,0,0,"Pc123",50.0,"C123","5","USA",63,"Adult"]
new_data=pd.DataFrame({"Name":["홍길동", "bob"], "Age":[22,30], "Sex":["female","male"], "Survived":[1,0]})
titanic=pd.concat([titanic, new_data], ignore_index=True)
print(titanic.tail())

#titanic[Name].str.startswith("Sa") Name열에서 S로 시작하는 이름 찾기
#titanic["Age"].astype(str).str.startswith("2") Age열에서 2로 시작하는 나이 찾기

#파일 저장
titanic.to_csv("./sample1.csv", index=False)
titanic.to_excel("./sample1.xlsx", index=False)