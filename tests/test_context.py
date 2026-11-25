"""验证业务输入之间的引用关系及形状，不计算目标输出。"""
import numpy as np
from support.inspect_data import load_bundle

def test_linked_materials():
    _, arrays, r, scenarios = load_bundle()
    all_ids=[]
    for frame in r['frames']:
        assert set(frame['tiles'])<=set(r['expected_tiles'])
        for box in frame['detections']:
            all_ids.append(box['candidate_id'])
            assert box['tile'] in frame['offsets'] and box['tile'] in frame['coverage']
            x1,y1,x2,y2=box['box']; assert x1<x2 and y1<y2
    assert len(set(all_ids)) == len(all_ids)
