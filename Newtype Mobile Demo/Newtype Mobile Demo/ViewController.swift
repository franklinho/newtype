//
//  ViewController.swift
//  Newtype Mobile Demo
//
//  Created by Franklin Ho on 1/26/15.
//  Copyright (c) 2015 Franklin Ho. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var demosTableView: UITableView!
    
    var demos = ["Best Buy", "Candy Crush Soda Saga"]
    var demosCategories = ["Best Buy": "E-Commerce","Candy Crush Soda Saga":"Gaming"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.demosTableView.delegate = self
        self.demosTableView.dataSource = self
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        
        
        var demo = demos[indexPath.row]
        
        var cell : AnyObject
        
        if demo == "Best Buy" {
            cell = demosTableView.dequeueReusableCellWithIdentifier("BestBuyTableViewCell") as BestBuyTableViewCell
            (cell as BestBuyTableViewCell).demoNameLabel.text = demo as String
            (cell as BestBuyTableViewCell).demoCategoryLabel.text = demosCategories[demo]
            
        } else {
            cell = demosTableView.dequeueReusableCellWithIdentifier("CandyCrushTableViewCell") as CandyCrushTableViewCell
            (cell as CandyCrushTableViewCell).demoNameLabel.text = demo as String
            (cell as CandyCrushTableViewCell).demoCategoryLabel.text = demosCategories[demo]

        }
        
        
        
        return cell as UITableViewCell
        
    }

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.demos.count
    }

}

