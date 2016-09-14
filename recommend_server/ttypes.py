#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class PageT:
  BANNER = 1
  CART_LIST = 2
  STRATEGY_LIST = 3
  GIFT_FRONT = 4
  ARTICLE_LIST = 5
  PRODUCT_DETAIL = 6

  _VALUES_TO_NAMES = {
    1: "BANNER",
    2: "CART_LIST",
    3: "STRATEGY_LIST",
    4: "GIFT_FRONT",
    5: "ARTICLE_LIST",
    6: "PRODUCT_DETAIL",
  }

  _NAMES_TO_VALUES = {
    "BANNER": 1,
    "CART_LIST": 2,
    "STRATEGY_LIST": 3,
    "GIFT_FRONT": 4,
    "ARTICLE_LIST": 5,
    "PRODUCT_DETAIL": 6,
  }

class RecommendTypeT:
  DEFAULT_TYPE = 0
  VIEW_THEN_VIEW = 1
  BUY_THEN_BUY = 2
  GUESS_LIKE = 3

  _VALUES_TO_NAMES = {
    0: "DEFAULT_TYPE",
    1: "VIEW_THEN_VIEW",
    2: "BUY_THEN_BUY",
    3: "GUESS_LIKE",
  }

  _NAMES_TO_VALUES = {
    "DEFAULT_TYPE": 0,
    "VIEW_THEN_VIEW": 1,
    "BUY_THEN_BUY": 2,
    "GUESS_LIKE": 3,
  }


class UserLocationT:
  """
  Attributes:
   - latitude
   - longtitude
   - province
   - city
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'latitude', None, None, ), # 1
    (2, TType.DOUBLE, 'longtitude', None, None, ), # 2
    (3, TType.STRING, 'province', None, None, ), # 3
    (4, TType.STRING, 'city', None, None, ), # 4
  )

  def __init__(self, latitude=None, longtitude=None, province=None, city=None,):
    self.latitude = latitude
    self.longtitude = longtitude
    self.province = province
    self.city = city

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.latitude = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.longtitude = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.province = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.city = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('UserLocationT')
    if self.latitude is not None:
      oprot.writeFieldBegin('latitude', TType.DOUBLE, 1)
      oprot.writeDouble(self.latitude)
      oprot.writeFieldEnd()
    if self.longtitude is not None:
      oprot.writeFieldBegin('longtitude', TType.DOUBLE, 2)
      oprot.writeDouble(self.longtitude)
      oprot.writeFieldEnd()
    if self.province is not None:
      oprot.writeFieldBegin('province', TType.STRING, 3)
      oprot.writeString(self.province)
      oprot.writeFieldEnd()
    if self.city is not None:
      oprot.writeFieldBegin('city', TType.STRING, 4)
      oprot.writeString(self.city)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.latitude)
    value = (value * 31) ^ hash(self.longtitude)
    value = (value * 31) ^ hash(self.province)
    value = (value * 31) ^ hash(self.city)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UserContextT:
  """
  Attributes:
   - time
   - page
   - userLocation
   - showGoodIdList
   - cartGoodIdLIst
   - favorGoodIdLIst
   - strategyTitle
   - strategyText
   - articleTitleList
   - articleText
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'time', None, None, ), # 1
    None, # 2
    (3, TType.I32, 'page', None, None, ), # 3
    (4, TType.STRUCT, 'userLocation', (UserLocationT, UserLocationT.thrift_spec), None, ), # 4
    (5, TType.LIST, 'showGoodIdList', (TType.I64,None), None, ), # 5
    (6, TType.LIST, 'cartGoodIdLIst', (TType.I64,None), None, ), # 6
    (7, TType.LIST, 'favorGoodIdLIst', (TType.I64,None), None, ), # 7
    (8, TType.STRING, 'strategyTitle', None, None, ), # 8
    (9, TType.STRING, 'strategyText', None, None, ), # 9
    (10, TType.LIST, 'articleTitleList', (TType.STRING,None), None, ), # 10
    (11, TType.STRING, 'articleText', None, None, ), # 11
  )

  def __init__(self, time=None, page=None, userLocation=None, showGoodIdList=None, cartGoodIdLIst=None, favorGoodIdLIst=None, strategyTitle=None, strategyText=None, articleTitleList=None, articleText=None,):
    self.time = time
    self.page = page
    self.userLocation = userLocation
    self.showGoodIdList = showGoodIdList
    self.cartGoodIdLIst = cartGoodIdLIst
    self.favorGoodIdLIst = favorGoodIdLIst
    self.strategyTitle = strategyTitle
    self.strategyText = strategyText
    self.articleTitleList = articleTitleList
    self.articleText = articleText

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.time = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.page = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.userLocation = UserLocationT()
          self.userLocation.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.showGoodIdList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI64()
            self.showGoodIdList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.cartGoodIdLIst = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readI64()
            self.cartGoodIdLIst.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.favorGoodIdLIst = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = iprot.readI64()
            self.favorGoodIdLIst.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.strategyTitle = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.strategyText = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.articleTitleList = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in xrange(_size18):
            _elem23 = iprot.readString()
            self.articleTitleList.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.articleText = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('UserContextT')
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I64, 1)
      oprot.writeI64(self.time)
      oprot.writeFieldEnd()
    if self.page is not None:
      oprot.writeFieldBegin('page', TType.I32, 3)
      oprot.writeI32(self.page)
      oprot.writeFieldEnd()
    if self.userLocation is not None:
      oprot.writeFieldBegin('userLocation', TType.STRUCT, 4)
      self.userLocation.write(oprot)
      oprot.writeFieldEnd()
    if self.showGoodIdList is not None:
      oprot.writeFieldBegin('showGoodIdList', TType.LIST, 5)
      oprot.writeListBegin(TType.I64, len(self.showGoodIdList))
      for iter24 in self.showGoodIdList:
        oprot.writeI64(iter24)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.cartGoodIdLIst is not None:
      oprot.writeFieldBegin('cartGoodIdLIst', TType.LIST, 6)
      oprot.writeListBegin(TType.I64, len(self.cartGoodIdLIst))
      for iter25 in self.cartGoodIdLIst:
        oprot.writeI64(iter25)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.favorGoodIdLIst is not None:
      oprot.writeFieldBegin('favorGoodIdLIst', TType.LIST, 7)
      oprot.writeListBegin(TType.I64, len(self.favorGoodIdLIst))
      for iter26 in self.favorGoodIdLIst:
        oprot.writeI64(iter26)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.strategyTitle is not None:
      oprot.writeFieldBegin('strategyTitle', TType.STRING, 8)
      oprot.writeString(self.strategyTitle)
      oprot.writeFieldEnd()
    if self.strategyText is not None:
      oprot.writeFieldBegin('strategyText', TType.STRING, 9)
      oprot.writeString(self.strategyText)
      oprot.writeFieldEnd()
    if self.articleTitleList is not None:
      oprot.writeFieldBegin('articleTitleList', TType.LIST, 10)
      oprot.writeListBegin(TType.STRING, len(self.articleTitleList))
      for iter27 in self.articleTitleList:
        oprot.writeString(iter27)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.articleText is not None:
      oprot.writeFieldBegin('articleText', TType.STRING, 11)
      oprot.writeString(self.articleText)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.time is None:
      raise TProtocol.TProtocolException(message='Required field time is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.time)
    value = (value * 31) ^ hash(self.page)
    value = (value * 31) ^ hash(self.userLocation)
    value = (value * 31) ^ hash(self.showGoodIdList)
    value = (value * 31) ^ hash(self.cartGoodIdLIst)
    value = (value * 31) ^ hash(self.favorGoodIdLIst)
    value = (value * 31) ^ hash(self.strategyTitle)
    value = (value * 31) ^ hash(self.strategyText)
    value = (value * 31) ^ hash(self.articleTitleList)
    value = (value * 31) ^ hash(self.articleText)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
