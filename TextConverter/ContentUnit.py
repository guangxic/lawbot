
class NoKeyFactorException(Exception):
    def __init__(self):
      None

class ContentUnit:
    _FACTOR_LIST = ["被告向原告借款",
                    "借款人由被告提供担保向原告借款",
                    "双方约定借款利息",
                    "双方约定逾期利息",
                    "双方约定借款期限",
                    "双方未约定利息",
                    "双方未约定还款期限",
                    "被告出具借条",
                    "被告拖欠借款",
                    "借款人拖欠借款",
                    "在借款给被告时原告收了部分利息",
                    "部分借款双方约定借款利息",
                    "口头双方约定借款利息",
                    "被告的家人替被告偿还了部分借款",
                    "被告仅偿还了部分借款",
                    "被告拖欠剩余借款",
                    "被告还欠借款",
                    "被告为对借款承担连带责任",
                    "双方约定担保期限",
                    "被告为此债务的担保人",
                    "被告出具了还款保证书",
                    "两被告是夫妻关系",
                    "借款发生在两被告夫妻关系存续期间",
                    "被告未履行担保义务",
                    "被告支付了部分利息",
                    "原告起诉要求判令",
                    "被告向原告还款",
                    "支付利息",
                    "支付逾期利息",
                    "被告承担诉讼费",
                    "约定管辖法院",
                    "被告承担原告的交通费",
                    "约定如果逾期被告承担原告的交通费",
                    "约定如果逾期被告支付违约金",
                    "借条证明",
                    "担保函证明",
                    "转账凭证",
                    "婚姻状况证明",
                    "交通费证明",
                    "交通费",
                    "借款现金支付",
                    "借款转账支付",
                    "借款部分现金部分转账支付",
                    "被告未出席答辩",
                    "被告承认借款",
                    "被告不承认借款",
                    "被告承认还欠原告部分借款",
                    "被告向第三方借款",
                    "两被告已离婚"]

    def __init__(self, factor, text):
        if factor not in self._FACTOR_LIST:
            raise NoKeyFactorException

        self.factor = factor
        self.text = text