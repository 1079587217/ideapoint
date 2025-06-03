const CryptoJS = require("crypto-js")
const JSEncrypt = require("node-jsencrypt")
rsaEncrypt = function (t) {
    var e = new JSEncrypt;
    return e.setPublicKey("-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDnOWe/gs033L/2/xR3oi6SLAMPBY5VledUqqH6dbCNOdrGX4xW+1x6NUfvmwpHRBA2C7xWDDvOIldTl0rMtERTDy9homrVqEcW6/TY+dSVFL3e2Yg2sVaehHv7FhmATkgfC2FcXt8Wvm99QpKRSrGKpcFYJwOj2F8hJh+rTG0IPQIDAQAB-----END PUBLIC KEY-----"),
        e.encrypt(t)
}

encrypt = function (t) {
    t = JSON.stringify(t);
    var e = "c4i6eo3p8mk84uj4"
        , n = "c4i6eo3p8mk84uj4"
    return {
        i: CryptoJS.AES.encrypt(t, CryptoJS.enc.Utf8.parse(e), {
            iv: CryptoJS.enc.Utf8.parse(n)
        }).toString(),
        k: rsaEncrypt(e + n)
    }
}

var e = {
    "points": [
        [
            832,
            1978,
            22
        ],
        [
            833,
            1978,
            29
        ],
        [
            836,
            1978,
            38
        ],
        [
            839,
            1978,
            45
        ],
        [
            843,
            1978,
            55
        ],
        [
            849,
            1978,
            61
        ],
        [
            853,
            1978,
            70
        ],
        [
            858,
            1978,
            77
        ],
        [
            862,
            1978,
            86
        ],
        [
            868,
            1978,
            93
        ],
        [
            873,
            1978,
            101
        ],
        [
            876,
            1978,
            108
        ],
        [
            884,
            1978,
            116
        ],
        [
            889,
            1977,
            124
        ],
        [
            896,
            1976,
            132
        ],
        [
            903,
            1975,
            141
        ],
        [
            910,
            1974,
            148
        ],
        [
            914,
            1974,
            157
        ],
        [
            919,
            1974,
            164
        ],
        [
            923,
            1974,
            173
        ],
        [
            926,
            1974,
            180
        ],
        [
            929,
            1974,
            189
        ],
        [
            931,
            1974,
            196
        ],
        [
            933,
            1973,
            204
        ],
        [
            934,
            1973,
            213
        ],
        [
            936,
            1973,
            220
        ],
        [
            939,
            1972,
            228
        ],
        [
            941,
            1972,
            236
        ],
        [
            942,
            1972,
            244
        ],
        [
            944,
            1971,
            253
        ],
        [
            945,
            1971,
            261
        ],
        [
            947,
            1971,
            277
        ]
    ],
    "distanceX": 0.3568200080353556,
    "fp": "133be70b3ccac919d35d07deb7a1be7d",
    "address": "https://www.yunpian.com",
    "yp_riddler_id": "b15a106d-db45-45d5-a33f-69e6071c9145"
}

// a =encrypt(e)

function get_data(point, distance) {
    var e = {
        "points": point,
        "distanceX": (304 - 66) * (distance / (304 - 42)) / 304,
        "fp": "133be70b3ccac919d35d07deb7a1be7d",
        "address": "https://www.yunpian.com",
        "yp_riddler_id": "b15a106d-db45-45d5-a33f-69e6071c9145"
    }
    return encrypt(e)
}

// console.log(a)