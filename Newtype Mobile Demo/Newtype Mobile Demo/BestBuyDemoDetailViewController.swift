//
//  BestBuyDemoDetailViewController.swift
//  Newtype Mobile Demo
//
//  Created by Franklin Ho on 1/26/15.
//  Copyright (c) 2015 Franklin Ho. All rights reserved.
//

import UIKit

class BestBuyDemoDetailViewController: UIViewController {
    
    @IBOutlet weak var buyButton: UIButton!
    var productID : Int?

    @IBOutlet weak var productDetailImageView: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        var buttonLayer : CALayer = buyButton.layer
        
        buttonLayer.masksToBounds = true
        buttonLayer.cornerRadius = 5.0
        
        if self.productID != nil {
            self.productDetailImageView.image = UIImage(named: "\(productID!)d.jpg")
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */
    
    override func viewDidAppear(animated: Bool) {
        if self.productID != nil {
            self.productDetailImageView.image = UIImage(named: "\(productID!)d.jpg")
            println("\(productID)d.jpg")
        }
    }

}
