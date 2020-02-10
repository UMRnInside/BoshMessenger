// BoshMessenger, Licensed under WTFPL
// Author: UMRnInside

// will be array
fortunes = null;
bosh = null;

function loadData()
{
    var req = new XMLHttpRequest();
    req.open('GET', '../data.json');

    req.onload = function() {
        if (req.status == 200) {
            //console.log(req.responseText);
            var jsonobj = JSON.parse(req.responseText);
            var af, bf, fort;
            fortunes = new Array();

            for (af in jsonobj.after) 
            {
                for (bf in jsonobj.before)
                {
                    for (fort in jsonobj.famous)
                    {
                        var as = jsonobj.after[af];
                        var bs = jsonobj.before[bf];
                        var fs = jsonobj.famous[fort];
                        var tstr = fs.replace(/a/, bs).replace(/b/, as);
                        fortunes.push(tstr.replace(/x/g, "这件事"));
                    }
                }
            }

            bosh = new Array();
            for (b in jsonobj.bosh)
            {
                var text = jsonobj.bosh[b].replace(/x/g, "这件事");
                bosh.push(text);
            }
        } else {
            console.log("Failed");
        }
    };

    // Handle network errors
    req.onerror = function() {
        console.log("Network Error");
    };

    // Make the request
    req.send();
}

loadData();
