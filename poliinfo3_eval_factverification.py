#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import json
import pathlib
import math
from collections import Counter
from typing import Tuple, Dict


def get_args():
    parser = argparse.ArgumentParser(
        description="""NTCIR-16 QA Lab PoliInfo Fact Verificationタスクの自動評価スクリプトです．""")

    parser.add_argument('-i', '--input-files',
                        nargs='+',
                        required=True,
                        help='評価対象のJSONファイルを指定します')

    parser.add_argument('-g', '--gs-data',
                        required=True,
                        help='GSデータを指定します'
                        )

    return parser.parse_args()


def load_gs(path) -> Dict[str, Tuple[int, int, int, int]]:
    gs = {}
    with open(path, "r", encoding="utf-8-sig") as f:
        gs = json.load(f)

    gs_map = {}  # type: Dict[str, Tuple[int, int, int, int]]
    for ins in gs:
        i = ins['ID'].split('-')[-1]
        gs_map[i] = (int(ins['StartingLine']), int(ins['EndingLine']), int(ins['StartingLine']),
                     int(ins['EndingLine']))
    return gs_map


def main():
    args = get_args()
    input_files = args.input_files
    # GS読み込み
    gs_map = load_gs(args.gs_data)
    headers = ['Group ID', 'Priority', 'Recall', 'Precision', 'Q-Recall', 'Q-Precision', 'A-Recall', 'A-Precision',
               'lines', 'output', 'match', 'Q-lines', 'Q-output', 'Q-match', 'A-lines', 'A-output', 'A-match']

    # 評価データ各々に対して
    for path in args.input_files:
        ## RecallとPrecisionのもと
        nums_line = Counter()
        nums_output = Counter()
        nums_match = Counter()
        all_num = 0
        all_p = 0
        all_r = 0
        all_f = 0

        # JSON読み込み
        with open(path, "r", encoding="utf-8-sig") as f:
            rheaders = ['ID', 'Precision', 'Recall',
                        'Q-解答', 'Q-正解', 'Q-一致', 'Q-Precision', 'Q-Recall',
                        'A-解答', 'A-正解', 'A-一致', 'A-Precision', 'A-Recall','ALL_NUM','ALL_P','ALL_R','p','r','f']
            for ins in json.load(f):
                i = ins['ID'].split('-')[-1]
                qstart = int(ins['StartingLine'])
                qend = int(ins['EndingLine'])
                astart = int(ins['StartingLine'])
                aend = int(ins['EndingLine'])

                qoutput_lines = set(range(qstart, qend + 1))
                qcorrect_lines = set(range(gs_map[i][0], gs_map[i][1] + 1))
                aoutput_lines = set(range(astart, aend + 1))
                acorrect_lines = set(range(gs_map[i][2], gs_map[i][3] + 1))
                tmp_p = len(qcorrect_lines & qoutput_lines) / len(qoutput_lines) if len(
                        qoutput_lines) > 0 else math.nan
                tmp_r = len(qcorrect_lines & qoutput_lines) / len(qcorrect_lines)
                tmp_f = 2*tmp_r*tmp_p/(tmp_r+tmp_p) if (tmp_r + tmp_p) else 0
                all_p += tmp_p
                all_r += tmp_r
                all_f += tmp_f
                all_num +=1
                res = {
                    'ID': ins['ID'],
                    'Precision': (len(acorrect_lines & aoutput_lines) + len(qcorrect_lines & qoutput_lines)) / (
                            len(aoutput_lines) + len(qoutput_lines)),
                    'Recall': (len(acorrect_lines & aoutput_lines) + len(qcorrect_lines & qoutput_lines)) / (
                            len(acorrect_lines) + len(qcorrect_lines)),
                    'Q-解答': '{0}-{1}'.format(qstart, qend),
                    'Q-正解': '{0}-{1}'.format(gs_map[i][0], gs_map[i][1]),
                    'Q-一致': len(qcorrect_lines & qoutput_lines),
                    'Q-Precision': len(qcorrect_lines & qoutput_lines) / len(qoutput_lines) if len(
                        qoutput_lines) > 0 else math.nan,
                    'Q-Recall': len(qcorrect_lines & qoutput_lines) / len(qcorrect_lines),
                    'A-解答': '{0}-{1}'.format(astart, aend),
                    'A-正解': '{0}-{1}'.format(gs_map[i][2], gs_map[i][3]),
                    'A-一致': len(acorrect_lines & aoutput_lines),
                    'A-Precision': len(acorrect_lines & aoutput_lines) / len(aoutput_lines) if len(
                        aoutput_lines) > 0 else math.nan,
                    'A-Recall': len(acorrect_lines & aoutput_lines) / len(acorrect_lines)
                }

                nums_line['S'] += (len(acorrect_lines) + len(qcorrect_lines))
                nums_line['Q'] += len(qcorrect_lines)
                nums_line['A'] += len(acorrect_lines)
                nums_output['S'] += (len(aoutput_lines) + len(qoutput_lines))
                nums_output['Q'] += len(qoutput_lines)
                nums_output['A'] += len(aoutput_lines)
                nums_match['S'] += (len(acorrect_lines & aoutput_lines) + len(qcorrect_lines & qoutput_lines))
                nums_match['Q'] += len(qcorrect_lines & qoutput_lines)
                nums_match['A'] += len(acorrect_lines & aoutput_lines)

            p = all_p / all_num
            r = all_r / all_num
            f = all_f / all_num
            #f =2*r*p/(r+p) if (r + p) else 0

            # マイクロ平均
            res = {
                'ID': 'マイクロ平均',
                'Precision': nums_match['S'] / nums_output['S'],
                'Recall': nums_match['S'] / nums_line['S'],
                'Q-解答': nums_output['Q'],
                'Q-正解': nums_line['Q'],
                'Q-一致': nums_match['Q'],
                'Q-Precision': nums_match['Q'] / nums_output['Q'],
                'Q-Recall': nums_match['Q'] / nums_line['Q'],
                'A-解答': nums_output['A'],
                'A-正解': nums_line['A'],
                'A-一致': nums_match['A'],
                'A-Precision': nums_match['A'] / nums_output['A'],
                'A-Recall': nums_match['A'] / nums_line['A'],
                'ALL_NUM':all_num,
                'ALL_P':all_p,
                'ALL_R':all_r,
                'p':p,
                'r':r,
                'f':f,
            }
        print(json.dumps({
             "status": "success", 
             "score": f,
             "scores": [f, p, r],
             "res": {k: res[k] for k in rheaders}
        }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
