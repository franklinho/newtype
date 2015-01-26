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
    
    var demos = ["Best Buy", "Clash of Clans"]
    var demosCategories = ["Best Buy": "E-Commerce","Clash of Clans":"Gaming"]
    
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
        var cell = demosTableView.dequeueReusableCellWithIdentifier("DemosTableViewCell") as DemosTableViewCell
        
        var demo = demos[indexPath.row]
        
        cell.demoNameLabel.text = demo as String
        cell.demoCategoryLabel.text = demosCategories[demo]
        
        return cell
    }

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.demos.count
    }

}

