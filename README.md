# PoliInfo3-FormalRun-FactVerification


## English

Fact Verification attempts to verify the credibility of political claims using predefined primary sources.  
The files "PoliInfo3_FactVerification_Formal_Test.json" and "PoliInfo3_FactVerification_Formal_Train.json" and "PoliInfo3_FactVerification_Formal_Gold.json" have a format of the political claim.  
They contain the following fields.

| Field Name            | Description                                                                                           | Example                                                                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                      | Number that uniquely identifies the claim.                                                                     | 1                                                                                                                                                                                                                                                   |
| Prefecture              | Place of the meeting.                                                                                   | 東京都                                                                                                                                                                                                                                              |
| Date                    | Date of the meeting.                                                                               | 2024/2/28                                                                                                                                                                                                                                           |
| Meeting                 | Title of the meeting.                                                                                 | 平成24年第１回定例会                                                                                                                                                                                                                                |
| Speaker                 | Speaker name of the utterance.                                                                         | 宮崎章（自民党）                                                                                                                                                                                                                                    |
| UtteranceSummary        | Summary of the utterance.                                                                       | 〔1〕被災地そして日本の未来のため東京は先頭に立つべき。知事の所見は。〔2〕「2020年の東京」計画に込めた決意は。〔3〕24年度予算に込めた思いは。                                                                                                       |
| UtteranceType           | Type of the utterance. "question" or "answer".                                                 | question                                                                                                                                                                                                                                            |
| ContextSummary          | Summary of the entire dialogue before and after the utterance.                                                                        | 日本の未来のため東京が先頭に。帰宅困難者対策をどう具体化か                                                                                                                                                                                          |
| ContextWord             | Topic word related to the utterance.                                                                       | 都政運営の基本姿勢                                                                                                                                                                                                                                  |
| RelatedUtteranceSummary | Another utterance related to the utterance.   Example: When "UtteranceType" is "answer", "RelatedUtteranceSummary" is a summary of the question from which the answer was based. | 〔1〕都は全国の先頭に立ち被災地復興を強力に後押ししていく。〔2〕都市のあるべき姿を世界に発信し先陣を切って行動を起こし日本の再浮上に繋がる努力をしたい。〔3〕予算を原動力に東京を成長と発展の軌道に乗せ東京から日本の再生を牽引すべく全力を尽くす。 |
| StartingLine            | Target value of the task. "Line" of the predefined primary source corresponding to "UtteranceSummary".  This field is -1 when "DocumentEntailment" is false.                                                                 | 22233                                                                                                                                                                                                                                               |
| EndingLine              | Target value of the task. "Line" of the predefined primary source corresponding to "UtteranceSummary".  This field is -1 when "DocumentEntailment" is false.                                                                | 22252                                                                                                                                                                                                                                               |
| DocumentEntailment      | Target value of the task. Whether the claim is credible or not.                                                                 | true                                                                                                                                                                                                                                                | 

The file "Pref13_tokyo.json" has a format of predefined primary source.  
It contains the following fields.

| Field Name            | Description                                                                                           | Example                                                                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID | Identification code |130001_230928_828|
| Line| Line number|8274|
| Prefecture | Prefecture name |東京都 |
| Volume | Volume |平成23年_第３回|
| Number | Day of the meeting |2|
| Year | Year|23|
| Month | Month |9|
| Day | Day |28|
| Title | Title |平成23年_第３回定例会(第12号)|
| Speaker | Speaker |石原慎太郎|
| Utterance | Utterance |鈴木あきまさ議員の代表質問にお答えいたします。|
  
Please refer to the URL below for further information.

https://poliinfo3.net/tasks/fact-verification/

## Japanese 

Fact Verificationは、入力テキスト（発言要約）と会議録が与えられたとき、その要約の内容が本当に会議録中に存在するかを判定し、存在する場合はその範囲を特定することを目的としています。 

https://poliinfo3.net/tasks/fact-verification/

| フィールド名            | 説明                                                                                           | サンプル                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                      | データを一意に識別する番号                                                                     | 1                                                                                                                                                                                                                                                   |
| Prefecture              | 会議の開催地                                                                                   | 東京都                                                                                                                                                                                                                                              |
| Date                    | 会議の開催年月日                                                                               | 2024/2/28                                                                                                                                                                                                                                           |
| Meeting                 | 会議の識別情報                                                                                 | 平成24年第１回定例会                                                                                                                                                                                                                                |
| Speaker                 | データの主要部。発言者                                                                         | 宮崎章（自民党）                                                                                                                                                                                                                                    |
| UtteranceSummary        | データの主要部。発言内容                                                                       | 〔1〕被災地そして日本の未来のため東京は先頭に立つべき。知事の所見は。〔2〕「2020年の東京」計画に込めた決意は。〔3〕24年度予算に込めた思いは。                                                                                                       |
| UtteranceType           | 発言の種類。question（質問） or answer（回答）                                                 | question                                                                                                                                                                                                                                            |
| ContextSummary          | 発言前後の対話全体の要約                                                                       | 日本の未来のため東京が先頭に。帰宅困難者対策をどう具体化か                                                                                                                                                                                          |
| ContextWord             | 発言が対象としている主題                                                                       | 都政運営の基本姿勢                                                                                                                                                                                                                                  |
| RelatedUtteranceSummary | 発言に関連する発言の要約。<br>例： UtteranceTypeが「回答」のとき、回答のもととなった質問の要約 | 〔1〕都は全国の先頭に立ち被災地復興を強力に後押ししていく。〔2〕都市のあるべき姿を世界に発信し先陣を切って行動を起こし日本の再浮上に繋がる努力をしたい。〔3〕予算を原動力に東京を成長と発展の軌道に乗せ東京から日本の再生を牽引すべく全力を尽くす。 |
| StartingLine            | 本タスクの予測対象。要約開始行。DocumentEntailmentがfalseの場合は-1                                                                 | 22233                                                                                                                                                                                                                                               |
| EndingLine              | 本タスクの予測対象。 要約終了行。DocumentEntailmentがfalseの場合は-1                                                                | 22252                                                                                                                                                                                                                                               |
| DocumentEntailment      | 本タスクの予測対象。情報の真偽                                                                 | true                                                                                                                                                                                                                                                | 
