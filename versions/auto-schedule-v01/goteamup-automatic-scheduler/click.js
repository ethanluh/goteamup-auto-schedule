function book(active){
	document.evaluate(active, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();	
}