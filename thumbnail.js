address = phantom.args[0];
outfile = phantom.args[1];
var page = require('webpage').create();
page.open(address, function (status) {
    page.render(outfile);
    phantom.exit();
});
