namespace java com.octinn.portrait.thrift
namespace php com.octinn.portrait.thrift

struct LocationT {
    1: optional double latitude;
    2: optional double longtitude;
    3: optional string province;
    4: optional string city;
}

enum Action {
    VIEW = 0;
    BUY = 1;
    COLLECTION = 2
    REMOVE_COLLECTION = 3
    CART = 4
    REMOVE_CART = 5
}

struct BehaviorT {
    1: required Action action;
    2: required i64 timestamp;
    3: optional i32 times;
    4: optional i32 duration;
}

struct UserProfileT {
    1: required i64 id;
    2: required string userName;
    3: required i64 registerTime;
    4: required i64 birthday;
    5: required string phone;
    6: required string email;
    7: required string weixin;
    8: required string weibo;
    9: required string constellation;
    10: required string device;
    11: required i32 birthRecord;
    12: required i32 age;
    13: required string sex;
    14: required i32 shoppingAbility;
    15: required list<string> tagFitSex;
    16: required list<list<i32>> tagFitAge;
    17: required list<string> tagFitScenario;
    18: required list<string> tagFitMaterial;
    19: required list<string> tagFitDesignStyle;
    20: required list<string> tagFitTarget;
    21: required list<string> tagFitPackage;
    22: required list<string> tagList;
    23: required i32 haveMate;
    24: required i32 haveChild;
    25: required i32 testServer;
    26: required i64 updateTime;
}

struct UserBehaviorT {

    1: required i64 id;
    2: required list<string> recent30DayViewList;
    3: required list<i32> recent30DayViewListCount;
    4: required list<string> recent30DayViewListTime;
    5: required i32 recent30DayViewTotalCount;
    6: required i32 recent30DayActiveViewTime;
    7: required string recent30DayActiveViewTimeRange;
    8: required list<string> recent30DayQueryList;
    9: required list<string> recent30DayQueryListTime;
    10: required string firstBuy;
    11: required i32 totalBuyCount;
    12: required double totalBuyFee;
    13: required double minOrderFee;
    14: required double maxOrderFee;
    15: required i32 recent30DayBuyTotalCount;
    16: required double recent30DayBuyTotalFee;
    17: required double recent30DayBuyMeanFee;
    18: required list<string> recent30DayBuyList;
    19: required list<i32> recent30DayBuyListCount;
    20: required list<string> recent30DayBuyListTime;
    21: required list<list<string>> recent30DayBuyCategory;
    22: required list<i32> recent30DayBuyCategoryCount;
    23: required list<string> recent30DayBuyBrand;
    24: required list<i32> recent30DayBuyBrandCount;
    25: required i32 recent90DayComplainCount;
    26: required i32 recent90DayRefuseCount;
    27: required double recent90DayRefuseRate;
    28: required i32 recent90DayRefundCount;
    29: required double recent90DayRefundRate;
    30: required i64 updateTime;
}

struct UserContextT {

    1: required i64 id;
    2: required string weather;
    3: required list<i64> favorList;
    4: required list<i64> shoppingCartList;
    5: required i32 recent30DayShoppingCartCount;
    6: required list<string> recent30DayShoppingCartBrandList;
    7: required list<list<string>> recent30DayShoppingCartCategoryList;
    8: required double recent30DayBoughtCartListDate;
    9: required i64 shoppingCartLatestUpdate;
    10: required i32 recent30DayBuyTotalCount;
    11: required list<string> recent30DayCollectionBrandList;
    12: required list<list<string>> recent30DayCollectionCategoryList;
    13: required i32 scoreAvail;
    14: required i32 scoreUsed;
    15: required i32 scoreTotal;
    16: required i32 couponAvail;
    17: required i32 couponUsed;
    18: required i32 couponTotal;
    19: required i32 couponAvailValue;
    20: required i32 couponUsedValue;
    21: required i32 couponTotalValue;
    22: required i32 shoppingCartLatestUpdateCount;
    23: required list<i32> recent30DayShoppingCartBoughtList;
    24: required i64 updateTime;
    25: optional list<LocationT> location;
}


struct GoodPortraitT {
    1: required i64 id;
    2: required string name;
    3: required double meanPrice;
    4: optional list<LocationT> location;
    5: required double score;
    6: required i16 heat;
    7: required i64 availableOn;
    8: required list<string> categoryName;
    9: required i16 enable;
    10: required string brandWebsite;
    11: required string brandName;
    12: required string brandPhone;
    13: required string description;
    14: required list<list<i32>> tagFitAge;
    15: required list<string> tagFitSex;
    16: required list<string> tagFitScenario;
    17: required list<string> tagFitTarget;
    18: required list<string> tagDesignStyle;
    19: required list<string> tagMaterial;
    20: required list<string> tagPackQuality;
    21: required list<string> tagList;
    22: required double newGood;
    23: required double hotGood;
    24: required list<i32> recent7DaySoldCount;
    25: required list<i32> recent7DayViewCount;
    26: required i32 recent7DayAddToCartCount;
    27: required i32 refuseCount;
    28: required double refuseRate;
    29: required double promotionSense;
    30: required i32 expressSpeed;
    31: required double discount;
    32: required i64 updateTime;
}

service OctinnPortraitThrift {

     UserProfileT getUserProfile(1: i64 userId);

     UserBehaviorT getUserBehavior(1: i64 userId);

     UserContextT getUserContext(1: i64 userId);

     GoodPortraitT getGoodPortrait(1: i64 goodId);

     list <GoodPortraitT> getGoodPortraitList(1: list<i64> goodIdList);
}