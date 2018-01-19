//alert("hello photoshop")
app.activeDocument.activeLayer.opacity = 60;
var newLayer = activeDocument.artLayers.add();
newLayer.name = "My layer";
var layerRef = activeDocument.artLayers.getByName("My layer")
/*var opts = new PDFOpenOptions();
opts.page = 10;
app.open(1.pdf,opts);*/
alert(app.font.length);
