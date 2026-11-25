from app.db import 连接


def 总览() -> dict:
    conn = 连接()
    try:
        def 数(sql: str) -> int:
            return int(conn.execute(sql).fetchone()[0])

        return {
            "账户数": 数("SELECT COUNT(*) FROM 账户"),
            "多币账户数": 数("SELECT COUNT(*) FROM 账户 WHERE 多币种=1"),
            "流水数": 数("SELECT COUNT(*) FROM 变动流水 WHERE 命运='已入账'"),
            "快照数": 数("SELECT COUNT(*) FROM 周期快照 WHERE 状态='有效'"),
            "分轨快照数": 数(
                "SELECT COUNT(*) FROM 周期快照 WHERE 状态='有效' AND TRIM(币种)<>''"
            ),
            "未标币种快照数": 数(
                "SELECT COUNT(*) FROM 周期快照 WHERE 状态='有效' AND (币种 IS NULL OR TRIM(币种)='')"
            ),
            "差额行数": 数("SELECT COUNT(*) FROM 差额行"),
            "断档数": 数("SELECT COUNT(*) FROM 断档记录"),
            "跳变数": 数("SELECT COUNT(*) FROM 跳变记录"),
            "混币旁置数": 数("SELECT COUNT(*) FROM 旁置簿 WHERE 原因 LIKE '币种闸:%'"),
            "旁置数": 数("SELECT COUNT(*) FROM 旁置簿"),
            "抽取批次数": 数("SELECT COUNT(*) FROM 抽取批次"),
            "回放批次数": 数("SELECT COUNT(*) FROM 回放批次"),
        }
    finally:
        conn.close()
