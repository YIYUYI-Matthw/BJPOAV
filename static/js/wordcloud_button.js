// 使用fetch发送GET请求，获取图片列表
fetch('/get_image_list')
    .then(response => response.json())
    .then(data => {
        // 获取图片列表
        const imageList = data.image_list;
        // 用文本渲染按钮
        renderButtons(imageList);
    })
    .catch(error => {
        console.error('Error:', error);
    });
// 渲染按钮和下拉菜单
function renderButtons(imageList) {
    const uploadButton = document.getElementById('upload-button');
    const dropdownContainer = document.getElementById('dropdown-container');
    // 创建下拉菜单的按钮
    const dropdownBtn = document.createElement('button');
    dropdownBtn.className = 'dropdown-btn';
    dropdownBtn.textContent = '选择词云图形';
    dropdownContainer.appendChild(dropdownBtn);
    // 创建下拉菜单内容容器
    const dropdownContent = document.createElement('div');
    dropdownContent.className = 'dropdown-content';
    dropdownContainer.appendChild(dropdownContent);
    let isDropdownVisible = false; // 记录下拉菜单是否可见的状态
    dropdownBtn.addEventListener('click', () => {
        if (isDropdownVisible) {
            dropdownContent.classList.remove('show');
        } else {
            dropdownContent.classList.add('show');
        }
        isDropdownVisible = !isDropdownVisible; // 切换下拉菜单可见状态
    });
    // 遍历图片列表，将图片渲染为下拉菜单的选项
    imageList.forEach(imageUrl => {
        const optionBtn = document.createElement('button');
        optionBtn.textContent = imageUrl;
        optionBtn.addEventListener('click', () => {
            console.log(imageUrl);
            getImageData(imageUrl);
        });
        dropdownContent.appendChild(optionBtn);
    });
    // 监听上传按钮的点击事件
    uploadButton.addEventListener('click', () => {
        // 创建文件选择的input元素
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = '.png';
        // 监听文件选择的change事件
        fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        // 创建文件读取器
        const reader = new FileReader();
        reader.onload = (event) => {
            const base64Data = event.target.result;
            // 绘制词云图形
            drawWordCloud(base64Data);
        };
        // 读取文件为base64数据
        reader.readAsDataURL(file);
        });
        // 触发文件选择对话框
        fileInput.click();
    });
}
// 获取图片数据
function getImageData(imageUrl) {
    // 使用fetch发送POST请求，获取Base64图片数据
    fetch('/get_base64_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'image_name': imageUrl })
    })
    .then(response => response.json())
    .then(data => {
        const base64Data = data.base64_data;
        // 在这里可以使用Base64图片数据进行操作，例如将其显示在页面上或下载
        drawWordCloud('data:image/png;base64,'+base64Data);
        // 隐藏下拉菜单
        const dropdownContent = document.querySelector('.dropdown-content');
        dropdownContent.classList.remove('show');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
//绘制词云图函数
function drawWordCloud(base64_data){
    //此处先暂且固定数据把
    var data = [
      {
          "name": "Uyghur",
          "value": 29661
      },
      {
          "name": "China",
          "value": 8659
      },
      {
          "name": "'s",
          "value": 6708
      },
      {
          "name": "Chinese",
          "value": 5521
      },
      {
          "name": "genocide",
          "value": 5515
      },
      {
          "name": "The",
          "value": 5381
      },
      {
          "name": "amp",
          "value": 5201
      },
      {
          "name": "``",
          "value": 5134
      },
      {
          "name": "I",
          "value": 5125
      },
      {
          "name": "''",
          "value": 4528
      },
      {
          "name": "Xinjiang",
          "value": 3925
      },
      {
          "name": "people",
          "value": 3887
      },
      {
          "name": "Muslims",
          "value": 3289
      },
      {
          "name": "right",
          "value": 3015
      },
      {
          "name": "Uyghurs",
          "value": 2963
      },
      {
          "name": "forced",
          "value": 2681
      },
      {
          "name": "camp",
          "value": 2633
      },
      {
          "name": "n't",
          "value": 2069
      },
      {
          "name": "human",
          "value": 2005
      },
      {
          "name": "year",
          "value": 1971
      },
      {
          "name": "government",
          "value": 1711
      },
      {
          "name": "labor",
          "value": 1676
      },
      {
          "name": "one",
          "value": 1672
      },
      {
          "name": "like",
          "value": 1574
      },
      {
          "name": "world",
          "value": 1573
      },
      {
          "name": "Muslim",
          "value": 1561
      },
      {
          "name": "woman",
          "value": 1552
      },
      {
          "name": "We",
          "value": 1551
      },
      {
          "name": "A",
          "value": 1450
      },
      {
          "name": "report",
          "value": 1446
      },
      {
          "name": "This",
          "value": 1414
      },
      {
          "name": "...",
          "value": 1383
      },
      {
          "name": "It",
          "value": 1355
      },
      {
          "name": "US",
          "value": 1317
      },
      {
          "name": "CCP",
          "value": 1309
      },
      {
          "name": "Chinas",
          "value": 1286
      },
      {
          "name": "region",
          "value": 1275
      },
      {
          "name": "say",
          "value": 1235
      },
      {
          "name": "country",
          "value": 1221
      },
      {
          "name": "Genocide",
          "value": 1220
      },
      {
          "name": "Forced",
          "value": 1206
      },
      {
          "name": "also",
          "value": 1182
      },
      {
          "name": "concentration",
          "value": 1182
      },
      {
          "name": "UN",
          "value": 1158
      },
      {
          "name": "support",
          "value": 1136
      },
      {
          "name": "community",
          "value": 1114
      },
      {
          "name": "campaign",
          "value": 1112
      },
      {
          "name": "said",
          "value": 1093
      },
      {
          "name": "victim",
          "value": 1083
      },
      {
          "name": "family",
          "value": 1058
      },
      {
          "name": "mass",
          "value": 1034
      },
      {
          "name": "know",
          "value": 1031
      },
      {
          "name": "East",
          "value": 1030
      },
      {
          "name": "Labor",
          "value": 1025
      },
      {
          "name": "group",
          "value": 1016
      },
      {
          "name": "crime",
          "value": 1005
      },
      {
          "name": "must",
          "value": 978
      },
      {
          "name": "u",
          "value": 969
      },
      {
          "name": "would",
          "value": 967
      },
      {
          "name": "made",
          "value": 954
      },
      {
          "name": "time",
          "value": 949
      },
      {
          "name": "Region",
          "value": 946
      },
      {
          "name": "million",
          "value": 941
      },
      {
          "name": "In",
          "value": 924
      },
      {
          "name": "many",
          "value": 918
      },
      {
          "name": "Act",
          "value": 900
      },
      {
          "name": "see",
          "value": 895
      },
      {
          "name": "together",
          "value": 878
      },
      {
          "name": "labour",
          "value": 868
      },
      {
          "name": "even",
          "value": 860
      },
      {
          "name": "new",
          "value": 856
      },
      {
          "name": "minority",
          "value": 828
      },
      {
          "name": "child",
          "value": 825
      },
      {
          "name": "company",
          "value": 813
      },
      {
          "name": "Beijing",
          "value": 808
      },
      {
          "name": "abuse",
          "value": 801
      },
      {
          "name": "language",
          "value": 799
      },
      {
          "name": "slave",
          "value": 798
      },
      {
          "name": "activist",
          "value": 797
      },
      {
          "name": "They",
          "value": 782
      },
      {
          "name": "culture",
          "value": 776
      },
      {
          "name": "call",
          "value": 776
      },
      {
          "name": "day",
          "value": 774
      },
      {
          "name": "population",
          "value": 760
      },
      {
          "name": "Prevention",
          "value": 753
      },
      {
          "name": "detained",
          "value": 747
      },
      {
          "name": "make",
          "value": 746
      },
      {
          "name": "issue",
          "value": 742
      },
      {
          "name": "life",
          "value": 739
      },
      {
          "name": "prison",
          "value": 737
      },
      {
          "name": "detention",
          "value": 731
      },
      {
          "name": "incarceration",
          "value": 730
      },
      {
          "name": "state",
          "value": 724
      },
      {
          "name": "today",
          "value": 712
      },
      {
          "name": "work",
          "value": 709
      },
      {
          "name": "take",
          "value": 705
      },
      {
          "name": "still",
          "value": 703
      },
      {
          "name": "stop",
          "value": 698
      },
      {
          "name": "good",
          "value": 695
      },
      {
          "name": "praying",
          "value": 692
      },
      {
          "name": "Pray",
          "value": 691
      },
      {
          "name": "get",
          "value": 683
      },
      {
          "name": "//",
          "value": 680
      },
      {
          "name": "You",
          "value": 676
      },
      {
          "name": "want",
          "value": 671
      },
      {
          "name": "What",
          "value": 666
      },
      {
          "name": "Urumqi.We",
          "value": 666
      },
      {
          "name": "Xinjiang.Name",
          "value": 666
      },
      {
          "name": "Profile",
          "value": 666
      },
      {
          "name": "Han",
          "value": 663
      },
      {
          "name": "Autonomous",
          "value": 661
      },
      {
          "name": "ethnic",
          "value": 659
      },
      {
          "name": "Turkistan",
          "value": 636
      },
      {
          "name": "If",
          "value": 631
      },
      {
          "name": "need",
          "value": 623
      },
      {
          "name": "Rights",
          "value": 623
      },
      {
          "name": "policy",
          "value": 617
      },
      {
          "name": "since",
          "value": 614
      },
      {
          "name": "Human",
          "value": 612
      },
      {
          "name": "visit",
          "value": 595
      },
      {
          "name": "think",
          "value": 587
      },
      {
          "name": "He",
          "value": 586
      },
      {
          "name": "protest",
          "value": 586
      },
      {
          "name": "part",
          "value": 585
      },
      {
          "name": "But",
          "value": 584
      },
      {
          "name": "first",
          "value": 577
      },
      {
          "name": "humanity",
          "value": 575
      },
      {
          "name": "story",
          "value": 572
      },
      {
          "name": "action",
          "value": 571
      },
      {
          "name": "member",
          "value": 568
      },
      {
          "name": "medium",
          "value": 565
      },
      {
          "name": "show",
          "value": 562
      },
      {
          "name": "UK",
          "value": 560
      },
      {
          "name": "including",
          "value": 553
      },
      {
          "name": "back",
          "value": 550
      },
      {
          "name": "way",
          "value": 545
      },
      {
          "name": "propaganda",
          "value": 544
      },
      {
          "name": "much",
          "value": 543
      },
      {
          "name": "end",
          "value": 542
      },
      {
          "name": "atrocity",
          "value": 540
      },
      {
          "name": "go",
          "value": 533
      },
      {
          "name": "student",
          "value": 531
      },
      {
          "name": "How",
          "value": 529
      },
      {
          "name": "using",
          "value": 528
      },
      {
          "name": "help",
          "value": 526
      },
      {
          "name": "use",
          "value": 526
      },
      {
          "name": "And",
          "value": 525
      },
      {
          "name": "Tibetan",
          "value": 524
      },
      {
          "name": "U.S.",
          "value": 522
      },
      {
          "name": "persecution",
          "value": 521
      },
      {
          "name": "never",
          "value": 518
      },
      {
          "name": "speak",
          "value": 513
      },
      {
          "name": "could",
          "value": 513
      },
      {
          "name": "face",
          "value": 513
      },
      {
          "name": "Xi",
          "value": 512
      },
      {
          "name": "stand",
          "value": 505
      },
      {
          "name": "official",
          "value": 501
      },
      {
          "name": "come",
          "value": 501
      },
      {
          "name": "friend",
          "value": 500
      },
      {
          "name": "thing",
          "value": 495
      },
      {
          "name": "Ukraine",
          "value": 490
      },
      {
          "name": "'re",
          "value": 489
      },
      {
          "name": "international",
          "value": 486
      },
      {
          "name": "Olympics",
          "value": 482
      },
      {
          "name": "treatment",
          "value": 482
      },
      {
          "name": "regime",
          "value": 480
      },
      {
          "name": "video",
          "value": 479
      },
      {
          "name": "Why",
          "value": 478
      },
      {
          "name": "evidence",
          "value": 478
      },
      {
          "name": "There",
          "value": 476
      },
      {
          "name": "..",
          "value": 474
      },
      {
          "name": "used",
          "value": 473
      },
      {
          "name": "refugee",
          "value": 473
      },
      {
          "name": "care",
          "value": 472
      },
      {
          "name": "supply",
          "value": 467
      },
      {
          "name": "going",
          "value": 465
      },
      {
          "name": "ongoing",
          "value": 465
      },
      {
          "name": "brother",
          "value": 463
      },
      {
          "name": "old",
          "value": 461
      },
      {
          "name": "man",
          "value": 461
      },
      {
          "name": "Hong",
          "value": 460
      },
      {
          "name": "World",
          "value": 457
      },
      {
          "name": "well",
          "value": 457
      },
      {
          "name": "death",
          "value": 454
      },
      {
          "name": "authority",
          "value": 454
      },
      {
          "name": "around",
          "value": 453
      },
      {
          "name": "reason",
          "value": 448
      },
      {
          "name": "police",
          "value": 448
      },
      {
          "name": "two",
          "value": 447
      },
      {
          "name": "look",
          "value": 447
      },
      {
          "name": "via",
          "value": 446
      },
      {
          "name": "killed",
          "value": 446
      },
      {
          "name": "My",
          "value": 445
      },
      {
          "name": "every",
          "value": 435
      },
      {
          "name": "So",
          "value": 433
      },
      {
          "name": "As",
          "value": 430
      },
      {
          "name": "name",
          "value": 429
      },
      {
          "name": "last",
          "value": 428
      },
      {
          "name": "Communist",
          "value": 426
      },
      {
          "name": "sentenced",
          "value": 424
      },
      {
          "name": "sister",
          "value": 420
      },
      {
          "name": "No",
          "value": 418
      },
      {
          "name": "freedom",
          "value": 417
      },
      {
          "name": "leader",
          "value": 415
      },
      {
          "name": "product",
          "value": 413
      },
      {
          "name": "book",
          "value": 411
      },
      {
          "name": "repression",
          "value": 410
      },
      {
          "name": "week",
          "value": 409
      },
      {
          "name": "chain",
          "value": 403
      },
      {
          "name": "cultural",
          "value": 401
      },
      {
          "name": "New",
          "value": 400
      },
      {
          "name": "dont",
          "value": 399
      },
      {
          "name": "oppression",
          "value": 398
      },
      {
          "name": "place",
          "value": 397
      },
      {
          "name": "Its",
          "value": 396
      },
      {
          "name": "war",
          "value": 396
      },
      {
          "name": "release",
          "value": 395
      },
      {
          "name": "home",
          "value": 394
      },
      {
          "name": "muslim",
          "value": 394
      },
      {
          "name": "th",
          "value": 392
      },
      {
          "name": "Kong",
          "value": 390
      },
      {
          "name": "organ",
          "value": 390
      },
      {
          "name": "history",
          "value": 389
      },
      {
          "name": "situation",
          "value": 383
      },
      {
          "name": "happening",
          "value": 379
      },
      {
          "name": "law",
          "value": 378
      },
      {
          "name": "school",
          "value": 378
      },
      {
          "name": "called",
          "value": 377
      },
      {
          "name": "Congress",
          "value": 375
      },
      {
          "name": "event",
          "value": 373
      },
      {
          "name": "violation",
          "value": 373
      },
      {
          "name": "innocent",
          "value": 370
      },
      {
          "name": "When",
          "value": 369
      },
      {
          "name": "long",
          "value": 369
      },
      {
          "name": "free",
          "value": 368
      },
      {
          "name": "Islamic",
          "value": 368
      },
      {
          "name": "Canada",
          "value": 367
      },
      {
          "name": "lie",
          "value": 367
      },
      {
          "name": "may",
          "value": 366
      },
      {
          "name": "torture",
          "value": 366
      },
      {
          "name": "kid",
          "value": 365
      },
      {
          "name": "really",
          "value": 364
      },
      {
          "name": "talk",
          "value": 363
      },
      {
          "name": "For",
          "value": 361
      },
      {
          "name": "live",
          "value": 357
      },
      {
          "name": "tell",
          "value": 355
      },
      {
          "name": "American",
          "value": 355
      },
      {
          "name": "Turkey",
          "value": 354
      },
      {
          "name": "Tibet",
          "value": 354
      },
      {
          "name": "Today",
          "value": 353
      },
      {
          "name": "global",
          "value": 352
      },
      {
          "name": "continue",
          "value": 351
      },
      {
          "name": "religious",
          "value": 350
      },
      {
          "name": "got",
          "value": 349
      },
      {
          "name": "suffering",
          "value": 346
      },
      {
          "name": "Thank",
          "value": 346
      },
      {
          "name": "Turkic",
          "value": 346
      },
      {
          "name": "find",
          "value": 346
      },
      {
          "name": "important",
          "value": 346
      },
      {
          "name": "claim",
          "value": 346
      },
      {
          "name": "ago",
          "value": 346
      },
      {
          "name": "risk",
          "value": 346
      },
      {
          "name": "Party",
          "value": 345
      },
      {
          "name": "food",
          "value": 345
      },
      {
          "name": "real",
          "value": 344
      },
      {
          "name": "calling",
          "value": 344
      },
      {
          "name": "keep",
          "value": 343
      },
      {
          "name": "men",
          "value": 341
      },
      {
          "name": "mean",
          "value": 340
      },
      {
          "name": "cotton",
          "value": 340
      },
      {
          "name": "solar",
          "value": 337
      },
      {
          "name": "United",
          "value": 335
      },
      {
          "name": "On",
          "value": 335
      },
      {
          "name": "'m",
          "value": 334
      },
      {
          "name": "great",
          "value": 333
      },
      {
          "name": "voice",
          "value": 333
      },
      {
          "name": "held",
          "value": 332
      },
      {
          "name": "living",
          "value": 332
      },
      {
          "name": "word",
          "value": 331
      },
      {
          "name": "concern",
          "value": 327
      },
      {
          "name": "girl",
          "value": 326
      },
      {
          "name": "Do",
          "value": 325
      },
      {
          "name": "homeland",
          "value": 323
      },
      {
          "name": "Saudi",
          "value": 323
      },
      {
          "name": "International",
          "value": 320
      },
      {
          "name": "join",
          "value": 320
      },
      {
          "name": "committing",
          "value": 320
      },
      {
          "name": "diaspora",
          "value": 318
      },
      {
          "name": "Russia",
          "value": 318
      },
      {
          "name": "give",
          "value": 316
      },
      {
          "name": "put",
          "value": 315
      },
      {
          "name": "believe",
          "value": 309
      },
      {
          "name": "next",
          "value": 309
      },
      {
          "name": "Is",
          "value": 309
      },
      {
          "name": "city",
          "value": 308
      },
      {
          "name": "political",
          "value": 306
      },
      {
          "name": "panel",
          "value": 306
      },
      {
          "name": "She",
          "value": 305
      },
      {
          "name": "WUC",
          "value": 304
      },
      {
          "name": "case",
          "value": 303
      },
      {
          "name": "read",
          "value": 301
      },
      {
          "name": "solidarity",
          "value": 298
      },
      {
          "name": "hope",
          "value": 297
      },
      {
          "name": "Free",
          "value": 297
      },
      {
          "name": "father",
          "value": 297
      },
      {
          "name": "President",
          "value": 297
      },
      {
          "name": "imprisoned",
          "value": 296
      },
      {
          "name": "news",
          "value": 296
      },
      {
          "name": "outside",
          "value": 296
      },
      {
          "name": "Where",
          "value": 296
      },
      {
          "name": "nothing",
          "value": 295
      },
      {
          "name": "mother",
          "value": 294
      },
      {
          "name": "'ve",
          "value": 294
      },
      {
          "name": "another",
          "value": 294
      },
      {
          "name": "let",
          "value": 292
      },
      {
          "name": "Western",
          "value": 291
      },
      {
          "name": "taken",
          "value": 291
      },
      {
          "name": "Now",
          "value": 291
      },
      {
          "name": "month",
          "value": 291
      },
      {
          "name": "surveillance",
          "value": 288
      },
      {
          "name": "sent",
          "value": 287
      },
      {
          "name": "survivor",
          "value": 287
      },
      {
          "name": "without",
          "value": 286
      },
      {
          "name": "Please",
          "value": 286
      },
      {
          "name": "told",
          "value": 286
      },
      {
          "name": "India",
          "value": 286
      },
      {
          "name": "act",
          "value": 285
      },
      {
          "name": "Pakistan",
          "value": 284
      },
      {
          "name": "speaking",
          "value": 283
      },
      {
          "name": "arrested",
          "value": 281
      },
      {
          "name": "That",
          "value": 280
      },
      {
          "name": "hold",
          "value": 280
      },
      {
          "name": "Not",
          "value": 279
      },
      {
          "name": "fact",
          "value": 279
      },
      {
          "name": "others",
          "value": 278
      },
      {
          "name": "fight",
          "value": 277
      },
      {
          "name": "Turkish",
          "value": 277
      },
      {
          "name": "taking",
          "value": 277
      },
      {
          "name": "trying",
          "value": 276
      },
      {
          "name": "saying",
          "value": 276
      },
      {
          "name": "western",
          "value": 274
      },
      {
          "name": "business",
          "value": 273
      },
      {
          "name": "account",
          "value": 273
      },
      {
          "name": "found",
          "value": 272
      },
      {
          "name": "To",
          "value": 271
      },
      {
          "name": "scholar",
          "value": 271
      },
      {
          "name": "Read",
          "value": 267
      },
      {
          "name": "internment",
          "value": 267
      },
      {
          "name": "West",
          "value": 265
      },
      {
          "name": "narrative",
          "value": 265
      },
      {
          "name": "effort",
          "value": 265
      },
      {
          "name": "across",
          "value": 265
      },
      {
          "name": "di",
          "value": 265
      },
      {
          "name": "due",
          "value": 264
      },
      {
          "name": "Turkestan",
          "value": 263
      },
      {
          "name": "govt",
          "value": 263
      },
      {
          "name": "Palestine",
          "value": 263
      },
      {
          "name": "question",
          "value": 263
      },
      {
          "name": "least",
          "value": 262
      },
      {
          "name": "vote",
          "value": 262
      },
      {
          "name": "nation",
          "value": 261
      },
      {
          "name": "Taiwan",
          "value": 261
      },
      {
          "name": "Our",
          "value": 260
      },
      {
          "name": "ca",
          "value": 260
      },
      {
          "name": "done",
          "value": 259
      },
      {
          "name": "import",
          "value": 259
      },
      {
          "name": "An",
          "value": 259
      },
      {
          "name": "Im",
          "value": 258
      },
      {
          "name": "identity",
          "value": 256
      },
      {
          "name": "ask",
          "value": 255
      },
      {
          "name": "Day",
          "value": 255
      },
      {
          "name": "force",
          "value": 255
      },
      {
          "name": "imprisonment",
          "value": 254
      },
      {
          "name": "cause",
          "value": 253
      },
      {
          "name": "Parliament",
          "value": 253
      },
      {
          "name": "Shame",
          "value": 252
      },
      {
          "name": "point",
          "value": 252
      },
      {
          "name": "lot",
          "value": 252
      },
      {
          "name": "silent",
          "value": 251
      },
      {
          "name": "etc",
          "value": 251
      },
      {
          "name": "Jinping",
          "value": 251
      },
      {
          "name": "thousand",
          "value": 249
      },
      {
          "name": "threat",
          "value": 249
      },
      {
          "name": "committed",
          "value": 248
      },
      {
          "name": "meet",
          "value": 248
      },
      {
          "name": "became",
          "value": 248
      },
      {
          "name": "Asia",
          "value": 247
      },
      {
          "name": "Just",
          "value": 247
      },
      {
          "name": "social",
          "value": 246
      },
      {
          "name": "enough",
          "value": 246
      },
      {
          "name": "Syria",
          "value": 246
      },
      {
          "name": "share",
          "value": 244
      },
      {
          "name": "always",
          "value": 244
      },
      {
          "name": "discus",
          "value": 244
      },
      {
          "name": "chief",
          "value": 244
      },
      {
          "name": "left",
          "value": 244
      },
      {
          "name": "better",
          "value": 242
      },
      {
          "name": "away",
          "value": 242
      },
      {
          "name": "journalist",
          "value": 242
      },
      {
          "name": "Islam",
          "value": 242
      },
      {
          "name": "already",
          "value": 241
      },
      {
          "name": "public",
          "value": 240
      },
      {
          "name": "released",
          "value": 240
      },
      {
          "name": "advocate",
          "value": 239
      },
      {
          "name": "hand",
          "value": 239
      },
      {
          "name": "died",
          "value": 238
      },
      {
          "name": "ban",
          "value": 238
      },
      {
          "name": "actually",
          "value": 236
      },
      {
          "name": "seen",
          "value": 236
      },
      {
          "name": "yet",
          "value": 236
      },
      {
          "name": "love",
          "value": 235
      },
      {
          "name": "Japan",
          "value": 234
      },
      {
          "name": "--",
          "value": 234
      },
      {
          "name": "ever",
          "value": 233
      },
      {
          "name": "statement",
          "value": 231
      },
      {
          "name": "Urumqi",
          "value": 231
      },
      {
          "name": "latest",
          "value": 231
      },
      {
          "name": "working",
          "value": 230
      },
      {
          "name": "source",
          "value": 230
      },
      {
          "name": "One",
          "value": 229
      },
      {
          "name": "demand",
          "value": 229
      },
      {
          "name": "Council",
          "value": 229
      },
      {
          "name": "among",
          "value": 228
      },
      {
          "name": "anything",
          "value": 228
      },
      {
          "name": "Was",
          "value": 227
      },
      {
          "name": "money",
          "value": 227
      },
      {
          "name": "person",
          "value": 226
      },
      {
          "name": "sure",
          "value": 226
      },
      {
          "name": "terrorist",
          "value": 226
      },
      {
          "name": "parent",
          "value": 225
      },
      {
          "name": "spoke",
          "value": 224
      },
      {
          "name": "front",
          "value": 224
      },
      {
          "name": "local",
          "value": 223
      },
      {
          "name": "national",
          "value": 223
      },
      {
          "name": "number",
          "value": 222
      },
      {
          "name": "past",
          "value": 222
      },
      {
          "name": "Olympic",
          "value": 221
      },
      {
          "name": "facing",
          "value": 221
      },
      {
          "name": "Afghanistan",
          "value": 221
      },
      {
          "name": "debate",
          "value": 221
      },
      {
          "name": "restaurant",
          "value": 220
      },
      {
          "name": "young",
          "value": 219
      },
      {
          "name": "so-called",
          "value": 218
      },
      {
          "name": "far",
          "value": 218
      },
      {
          "name": "meeting",
          "value": 218
      },
      {
          "name": "full",
          "value": 217
      },
      {
          "name": "organization",
          "value": 217
      },
      {
          "name": "May",
          "value": 217
      },
      {
          "name": "supporting",
          "value": 216
      },
      {
          "name": "response",
          "value": 216
      },
      {
          "name": "high",
          "value": 216
      },
      {
          "name": "foreign",
          "value": 215
      },
      {
          "name": "citizen",
          "value": 215
      },
      {
          "name": "guy",
          "value": 214
      },
      {
          "name": "continues",
          "value": 214
      },
      {
          "name": "Stop",
          "value": 214
      },
      {
          "name": "power",
          "value": 214
      },
      {
          "name": "step",
          "value": 214
      },
      {
          "name": "something",
          "value": 213
      },
      {
          "name": "party",
          "value": 212
      },
      {
          "name": "justice",
          "value": 212
      },
      {
          "name": "piece",
          "value": 212
      },
      {
          "name": "please",
          "value": 211
      },
      {
          "name": "went",
          "value": 211
      },
      {
          "name": "State",
          "value": 211
      },
      {
          "name": "raped",
          "value": 211
      },
      {
          "name": "talking",
          "value": 210
      },
      {
          "name": "article",
          "value": 210
      },
      {
          "name": "States",
          "value": 209
      },
      {
          "name": "known",
          "value": 209
      },
      {
          "name": "photo",
          "value": 209
      },
      {
          "name": "problem",
          "value": 208
      },
      {
          "name": "recent",
          "value": 208
      },
      {
          "name": "Arabia",
          "value": 208
      },
      {
          "name": "harvested",
          "value": 208
      },
      {
          "name": "English",
          "value": 207
      },
      {
          "name": "slavery",
          "value": 207
      },
      {
          "name": "experience",
          "value": 207
      },
      {
          "name": "making",
          "value": 205
      },
      {
          "name": "urge",
          "value": 204
      },
      {
          "name": "sanction",
          "value": 204
      },
      {
          "name": "team",
          "value": 204
      },
      {
          "name": "light",
          "value": 204
      },
      {
          "name": "forget",
          "value": 203
      },
      {
          "name": "met",
          "value": 203
      },
      {
          "name": "learn",
          "value": 202
      },
      {
          "name": "Australian",
          "value": 201
      },
      {
          "name": "lost",
          "value": 201
      },
      {
          "name": "Biden",
          "value": 201
      },
      {
          "name": "House",
          "value": 201
      },
      {
          "name": "remember",
          "value": 201
      },
      {
          "name": "whole",
          "value": 200
      },
      {
          "name": "everyone",
          "value": 199
      },
      {
          "name": "become",
          "value": 199
      },
      {
          "name": "change",
          "value": 199
      },
      {
          "name": "lockdown",
          "value": 199
      },
      {
          "name": "thought",
          "value": 198
      },
      {
          "name": "tie",
          "value": 198
      },
      {
          "name": "matter",
          "value": 197
      },
      {
          "name": "brand",
          "value": 197
      }
  ]
    var values = Object.values(data); // 获取权重值数组
    var minWeight = Math.min(...values); // 获取最小权重值
    var maxWeight = Math.max(...values); // 获取最大权重值
    var weightRange = [minWeight, maxWeight]; // 权重范围数组
    var fontSizeRange = [10, 40];
    // 根据权重值映射到字体大小
    function mapWeightToFontSize(weightList) {
        var fontSizeList = [];
        for (var i = 0; i < weightList.length; i++) {
            var weight = weightList[i];
            var normalizedWeight = (weight - weightRange[0]) / (weightRange[1] - weightRange[0]);
            var fontSize = fontSizeRange[0] + normalizedWeight * (fontSizeRange[1] - fontSizeRange[0]);
            fontSizeList.push(fontSize);
        }
        return fontSizeList;
    }
    var fontSize = mapWeightToFontSize(values);
        var myChart = echarts.init(document.getElementById('wordCloud'));
    var maskImage = new Image();
    maskImage.src = base64_data;
    maskImage.onload=function(){
        myChart.setOption({
        backgroundColor: "#fff",
        tooltip: {
          backgroundColor: 'rgba(0, 0, 0, 0)', // 设置Tooltip的背景色
          borderColor: '#333', // 设置Tooltip的边框颜色
          formatter: function (params) {
            return '权重: ' + params.data.value ;
          }
        },
        series: [
          {
            type: "wordCloud",
             // 鼠标拖动事件监听
            emphasis: {
                focus: 'self', // 只对当前词进行放大处理
                textStyle: {
                  fontSize: 55, // 设置放大后的字体大小
                },
                itemStyle: {
                  shadowColor: 'rgba(0, 0, 0, 0)',
                  shadowBlur: 0
                }
              },
              // 鼠标移出事件监听
            normal: {
                textStyle: {
                  fontSize: 16 // 恢复正常大小的字体大小
                }
            },
            gridSize: 3,//用来调整词之间的距离
            //shape: 'cardioid',
            //sizeRange: [6, 55],//用来调整字的大小范围
            rotationRange: [0,0],//用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
            rotationStep: 90,
            drawOutOfBound: false,// 允许词太大的时候，超出画布的范围
            layoutAnimation: false,// 布局的时候是否有动画
            maskImage: maskImage,//用来设置词云图的形状
            textStyle: {          //用来设置词的样式
              fontSize: fontSize,
              fontFamily:'sans-serif',
              fontWeight:'bold',
              color: function () {
                return 'rgb(' + [
                  Math.round(Math.random() * 250),
                  Math.round(Math.random() * 250),
                  Math.round(Math.random() * 250)
                ].join(',') + ')';
                }
            },
            left: "center",        //位置相关设置
            top: "center",
            right: null,
            bottom: null,
            //width: "100%",
            //height: "100%",
            data: data
          }
        ]
    })}
  }
