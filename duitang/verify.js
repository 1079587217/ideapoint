const CryptoJS = require("crypto-js");
// 示例调用



function  get_params(distance,array,time){
    // distance = 0.5142857142857142; // 明文数据
    key_tb = "59fcff86";         // 8字节密钥（16位十六进制）
    tb =CryptoJS.DES.encrypt(CryptoJS.enc.Utf8.parse(distance), CryptoJS.enc.Utf8.parse(key_tb), {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.ZeroPadding}).ciphertext.toString(CryptoJS.enc.Base64)
    // console.log(tb)
    // array =[
    //     [
    //         0,
    //         0,
    //         0
    //     ],
    //     [
    //         15,
    //         3,
    //         102
    //     ],
    //     [
    //         54,
    //         7,
    //         202
    //     ],
    //     [
    //         91,
    //         8,
    //         301
    //     ],
    //     [
    //         100,
    //         8,
    //         401
    //     ],
    //     [
    //         100,
    //         8,
    //         501
    //     ],
    //     [
    //         98,
    //         8,
    //         601
    //     ],
    //     [
    //         87,
    //         8,
    //         701
    //     ],
    //     [
    //         81,
    //         7,
    //         801
    //     ],
    //     [
    //         70,
    //         8,
    //         900
    //     ],
    //     [
    //         64,
    //         8,
    //         1002
    //     ],
    //     [
    //         61,
    //         8,
    //         1107
    //     ],
    //     [
    //         62,
    //         9,
    //         1200
    //     ],
    //     [
    //         92,
    //         10,
    //         1302
    //     ],
    //     [
    //         119,
    //         10,
    //         1402
    //     ],
    //     [
    //         119,
    //         10,
    //         1513
    //     ],
    //     [
    //         116,
    //         9,
    //         1601
    //     ],
    //     [
    //         109,
    //         7,
    //         1701
    //     ],
    //     [
    //         109,
    //         7,
    //         1810
    //     ],
    //     [
    //         108,
    //         7,
    //         1903
    //     ]
    // ]
    key_tm = "0569c403";
    tm =CryptoJS.DES.encrypt(CryptoJS.enc.Utf8.parse(JSON.stringify(array)), CryptoJS.enc.Utf8.parse(key_tm), {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.ZeroPadding}).ciphertext.toString(CryptoJS.enc.Base64)
    // console.log(tm)
    // time =1948
    key_ly = "65986a6b";
    ly =CryptoJS.DES.encrypt(CryptoJS.enc.Utf8.parse(time), CryptoJS.enc.Utf8.parse(key_ly), {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.ZeroPadding}).ciphertext.toString(CryptoJS.enc.Base64)
    // console.log(ly)
    return [tb,tm,ly]
}

