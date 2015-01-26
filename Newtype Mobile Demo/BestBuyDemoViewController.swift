//
//  BestBuyDemoViewController.swift
//  Newtype Mobile Demo
//
//  Created by Franklin Ho on 1/26/15.
//  Copyright (c) 2015 Franklin Ho. All rights reserved.
//

import UIKit

class BestBuyDemoViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var bestBuyDemoTableView: UITableView!
    
    var bestBuyProducts = [3365028,3478006,3986118,4349004]
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        self.bestBuyDemoTableView.delegate = self
        self.bestBuyDemoTableView.dataSource = self
        
        self.bestBuyDemoTableView.rowHeight = 260.0
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        var cell = bestBuyDemoTableView.dequeueReusableCellWithIdentifier("BestBuyDemoTableViewCell") as BestBuyDemoTableViewCell
        
        var product = bestBuyProducts[indexPath.row]
        
        cell.productOverviewImageView.image = UIImage(named: "\(product).jpg")
        
        return cell
        
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return bestBuyProducts.count
        
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if (segue.identifier == "BestBuyDetailSegue") {
            var bestBuyDetailViewController : BestBuyDemoDetailViewController = segue.destinationViewController as BestBuyDemoDetailViewController
            var productIndex = bestBuyDemoTableView.indexPathForSelectedRow()?.row
            bestBuyDetailViewController.productID = self.bestBuyProducts[productIndex!]
        }
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
